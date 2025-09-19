1. Create a conda environment
    conda create -n chatbot python=3.10 anaconda

2. Install dependencies
    pip install fastapi uvicorn langchain langchain-community langchain-ollama langchain-chroma langchain-huggingface sentence-transformers chromadb

    pip install pypdf

    Install Ollama -> https://ollama.com/download
    ollama pull deepseek-r1:1.5b
