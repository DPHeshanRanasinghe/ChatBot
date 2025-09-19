import glob
from pathlib import Path
from langchain_community.document_loaders import TextLoader, PyPDFLoader

def load_docs(folder="./docs"):
    docs = [] # Creates an empty list which will hold all loaded documents.
    for ext in ("*.txt", "*.md"):
        for file in glob.glob(str(Path(folder)/"**"/ext), recursive=True): # search all subfolders of folder for .txt and .md files
            docs.extend(TextLoader(file).load()) # Load the document and add it to the list
    for file in glob.glob(str(Path(folder)/"**/*.pdf"), recursive=True): # search all subfolders of folder for .pdf files
        docs.extend(PyPDFLoader(file).load()) # Load the document and add it to the list
    print(f"Loaded {len(docs)} documents from {folder}")
    return docs
