from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, validator
from typing import Optional
import os

from lib.clean import strip_think
from lib.load_docs import load_docs
from lib.build_rag import build_rag
from lib.get_vectorstore import get_vectorstore
from lib.logger import logger
from config import CORS_ORIGINS, LLM_MODEL

app = FastAPI(
    title="EduProvider Institute Chatbot API",
    description="RAG-based chatbot for InfoTech College of Business & IT",
    version="2.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

class Query(BaseModel):
    question: str
    
    @validator('question')
    def validate_question(cls, v):
        v = v.strip()
        if not v:
            raise ValueError('Question cannot be empty')
        if len(v) > 1000:
            raise ValueError('Question is too long (max 1000 characters)')
        return v

class ChatResponse(BaseModel):
    question: str
    answer: str
    status: str = "success"

class HealthResponse(BaseModel):
    status: str
    model: str
    docs_loaded: int

# Initialize on startup
logger.info("Initializing chatbot...")
try:
    docs = load_docs()
    vs = get_vectorstore(docs)
    qa = build_rag(vs)
    docs_count = len(docs)
    logger.info("Chatbot initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize chatbot: {e}")
    raise

@app.get("/", tags=["Info"])
def root():
    """Serve the chat UI."""
    html_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(html_path):
        return FileResponse(html_path)
    return {"message": "Welcome to the EduProvider Institute Chatbot API.", "version": "2.0.0"}

@app.get("/health", response_model=HealthResponse, tags=["Info"])
def health():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        model=LLM_MODEL,
        docs_loaded=docs_count
    )

@app.post("/chat", response_model=ChatResponse, tags=["Chat"])
def chat(query: Query):
    """Chat endpoint - ask a question and get an answer."""
    try:
        logger.info(f"Received question: {query.question[:50]}...")
        ans = qa.invoke(query.question)
        cleaned = strip_think(ans["result"])
        logger.info(f"Response generated successfully")
        return ChatResponse(
            question=query.question,
            answer=cleaned
        )
    except Exception as e:
        logger.error(f"Error processing chat request: {e}")
        raise HTTPException(status_code=500, detail=str(e))
