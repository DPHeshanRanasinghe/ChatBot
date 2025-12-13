
from lib.load_docs import load_docs
from lib.get_vectorstore import get_vectorstore
from lib.build_rag import build_rag
from lib.chat import chat
from lib.logger import logger


if __name__ == "__main__":
    try:
        logger.info("Starting ChatBot application...")
        
        docs = load_docs()
        if not docs:
            raise ValueError("No documents found in 'docs/'. Please add .txt, .md, or .pdf files.")
        
        vs = get_vectorstore(docs)
        rag_chain = build_rag(vs)
        chat(rag_chain)
        
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
    except Exception as e:
        logger.error(f"Application error: {e}")
        raise
