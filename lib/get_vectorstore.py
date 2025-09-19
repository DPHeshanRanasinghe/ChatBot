from pathlib import Path
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from lib.split_docs import split_docs

db_path = "./chromadb"

def get_vectorstore(docs):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2") # get the embeddings model
    if Path(db_path).exists() and any(Path(db_path).iterdir()): # check if the db_path directory exists and is not empty
        return Chroma(persist_directory=db_path, embedding_function=embeddings) # load the existing vectorstore
    chunks = split_docs(docs) # split the documents into smaller chunks
    print(f"Number of text chunks: {len(chunks)}")
    if not chunks:
        raise ValueError("No valid text chunks found. Check your documents in 'data/' folder.")
    vs = Chroma.from_documents(chunks, embeddings, persist_directory=db_path) # create a new vectorstore
    return vs
