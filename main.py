
from lib.load_docs import load_docs
from lib.get_vectorstore import get_vectorstore
from lib.build_rag import build_rag
from lib.chat import chat


if __name__ == "__main__":
    docs = load_docs()
    if not docs:
        raise ValueError("No documents found in 'docs/'. Please add .txt, .md, or .pdf files.")
    vs = get_vectorstore(docs)
    rag_chain = build_rag(vs)
    chat(rag_chain)
