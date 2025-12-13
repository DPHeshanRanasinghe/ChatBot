import glob
from pathlib import Path
from langchain_community.document_loaders import TextLoader, PyPDFLoader

from lib.logger import logger
from config import DOCS_FOLDER

def load_docs(folder: str = None):
    """Load documents from the specified folder.
    
    Args:
        folder: Path to documents folder. Defaults to DOCS_FOLDER from config.
    
    Returns:
        List of loaded documents.
    """
    folder = folder or DOCS_FOLDER
    docs = []
    
    # Load text and markdown files
    for ext in ("*.txt", "*.md"):
        for file in glob.glob(str(Path(folder)/"**"/ext), recursive=True):
            try:
                docs.extend(TextLoader(file).load())
                logger.debug(f"Loaded text file: {file}")
            except Exception as e:
                logger.error(f"Failed to load {file}: {e}")
    
    # Load PDF files
    for file in glob.glob(str(Path(folder)/"**/*.pdf"), recursive=True):
        try:
            docs.extend(PyPDFLoader(file).load())
            logger.debug(f"Loaded PDF file: {file}")
        except Exception as e:
            logger.error(f"Failed to load {file}: {e}")
    
    logger.info(f"Loaded {len(docs)} documents from {folder}")
    return docs
