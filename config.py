import os
from dotenv import load_dotenv

load_dotenv()

# Model Configuration
LLM_MODEL = os.getenv("LLM_MODEL", "deepseek-r1:1.5b")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0"))

# Document Processing
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "150"))
RETRIEVER_K = int(os.getenv("RETRIEVER_K", "4"))

# Paths
DOCS_FOLDER = os.getenv("DOCS_FOLDER", "./docs")
DB_PATH = os.getenv("DB_PATH", "./chromadb")

# API Settings
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
