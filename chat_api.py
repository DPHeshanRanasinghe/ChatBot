from fastapi import FastAPI
from pydantic import BaseModel

from lib.clean import strip_think
from lib.load_docs import load_docs
from lib.build_rag import build_rag
from lib.get_vectorstore import get_vectorstore

app = FastAPI(title="EduProvider Institute Chatbot API")

class Query(BaseModel):
    question: str

docs = load_docs()
vs = get_vectorstore(docs)
qa = build_rag(vs)

@app.get("/")
def root():
    return {"message": "Welcome to the EduProvider Institute Chatbot API."}

@app.post("/chat")
def chat(query: Query):
    ans = qa.invoke(query.question)
    cleaned = strip_think(ans["result"])
    return cleaned
