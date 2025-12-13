from pathlib import Path
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from lib.split_docs import split_docs
from lib.logger import logger
from config import DB_PATH, EMBEDDING_MODEL

def get_vectorstore(docs):
    """Get or create a vector store from documents.
    
    Args:
        docs: List of documents to vectorize.
    
    Returns:
        Chroma vector store instance.
    """
    logger.info(f"Initializing embeddings model: {EMBEDDING_MODEL}")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    
    # Check if existing vectorstore exists
    if Path(DB_PATH).exists() and any(Path(DB_PATH).iterdir()):
        logger.info(f"Loading existing vectorstore from {DB_PATH}")
        return Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    
    # Create new vectorstore
    chunks = split_docs(docs)
    if not chunks:
        raise ValueError("No valid text chunks found. Check your documents in 'docs/' folder.")
    
    logger.info(f"Creating new vectorstore with {len(chunks)} chunks at {DB_PATH}")
    vs = Chroma.from_documents(chunks, embeddings, persist_directory=DB_PATH)
    return vs
