# 🤖 InfoTech College Chatbot

A RAG (Retrieval-Augmented Generation) chatbot built with Python, LangChain, and FastAPI for **InfoTech College of Business & IT**. The chatbot answers questions about courses, admissions, and student support using document-based knowledge retrieval.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **🎨 Web Chat Interface**: Beautiful, responsive chat UI out of the box
- **🔍 RAG Pipeline**: Retrieval-Augmented Generation for accurate, context-aware responses
- **🚀 FastAPI Backend**: High-performance REST API with automatic OpenAPI documentation
- **🧠 LangChain Integration**: Modular document processing and chain building
- **🤖 Ollama LLM**: Local DeepSeek-r1:1.5b model for privacy and speed
- **📊 ChromaDB**: Vector database for efficient semantic search
- **🤗 HuggingFace Embeddings**: State-of-the-art text embeddings (all-MiniLM-L6-v2)
- **📄 Multi-format Support**: Parse PDF, TXT, and Markdown files
- **💬 Conversation Memory**: Optional chat history for contextual conversations
- **🔧 Configurable**: Environment variables for easy customization
- **📝 Logging**: Comprehensive logging for debugging and monitoring

## 🏗️ Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Documents     │ ──► │  Vector Store    │ ──► │   LLM (Ollama)  │
│  (PDF/TXT/MD)   │     │   (ChromaDB)     │     │  DeepSeek-r1    │
└─────────────────┘     └──────────────────┘     └─────────────────┘
        │                       │                        │
        ▼                       ▼                        ▼
   Load & Split          Embed & Store            Generate Answer
```

## 📁 Project Structure

```
ChatBot/
├── chat_api.py          # FastAPI REST API
├── main.py              # CLI interface
├── config.py            # Configuration management
├── .env.example         # Environment variables template
├── .gitignore           # Git ignore rules
├── requirements.txt     # Dependencies
├── static/
│   └── index.html       # Web chat interface
├── lib/
│   ├── load_docs.py     # Document loading (PDF, TXT, MD)
│   ├── split_docs.py    # Text chunking
│   ├── get_vectorstore.py # ChromaDB vector store
│   ├── build_rag.py     # RAG chain construction
│   ├── chat.py          # Interactive chat loop
│   ├── clean.py         # Response cleaning utilities
│   └── logger.py        # Logging configuration
├── docs/                # Knowledge base documents (add your PDFs here)
└── chromadb/            # Vector database storage (auto-generated)
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Conda (recommended) or pip
- [Ollama](https://ollama.com/download) installed

### Step 1: Clone the Repository

```bash
git clone https://github.com/DPHeshanRanasinghe/ChatBot.git
cd ChatBot
```

### Step 2: Set Up Environment

```bash
# Create conda environment
conda create -n chatbot python=3.10 -y
conda activate chatbot

# Or use venv
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Ollama

```bash
# Install Ollama from https://ollama.com/download
# Then pull the model
ollama pull deepseek-r1:1.5b
```

### Step 5: Configure (Optional)

```bash
# Copy example config
cp .env.example .env

# Edit .env with your settings
```

### Step 6: Add Documents

Place your PDF, TXT, or MD files in the `docs/` folder. These will be used as the knowledge base.

### Step 7: Run the Application

**Option A: Web UI Mode (Recommended)**
```bash
python -m uvicorn chat_api:app --reload
```
Then open http://localhost:8000 in your browser to use the chat interface.

**Option B: CLI Mode**
```bash
python main.py
```

## 🖥️ Screenshots

### Web Chat Interface
When you run the API and visit `http://localhost:8000`, you'll see a beautiful chat interface:

- 💬 Real-time chat with the AI assistant
- 🎯 Quick suggestion buttons for common questions
- ⌨️ Type your question and press Enter or click Send
- 📚 Links to API documentation at the bottom

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Web chat interface |
| GET | `/health` | Health check with model info |
| POST | `/chat` | Send a question, get an answer |
| GET | `/docs` | Swagger UI API documentation |

### Example API Usage

```bash
# Health check
curl http://localhost:8000/health

# Chat
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What courses do you offer?"}'
```

### Response Format

```json
{
  "question": "What courses do you offer?",
  "answer": "InfoTech College offers courses in...",
  "status": "success"
}
```

## ⚙️ Configuration

Configure via environment variables or `.env` file:

| Variable | Default | Description |
|----------|---------|-------------|
| `LLM_MODEL` | `deepseek-r1:1.5b` | Ollama model name |
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | HuggingFace embedding model |
| `TEMPERATURE` | `0` | LLM temperature (0 = deterministic) |
| `CHUNK_SIZE` | `1000` | Document chunk size |
| `CHUNK_OVERLAP` | `150` | Overlap between chunks |
| `RETRIEVER_K` | `4` | Number of documents to retrieve |
| `DOCS_FOLDER` | `./docs` | Path to documents folder |
| `DB_PATH` | `./chromadb` | Path to vector database |
| `CORS_ORIGINS` | `*` | Allowed CORS origins |

## 🛠️ Development

### Rebuild Vector Store

Delete the `chromadb/` folder to force rebuilding:

```bash
rm -rf chromadb/
python main.py
```

### Enable Debug Logging

```python
# In lib/logger.py, change:
logger.setLevel(logging.DEBUG)
```

### Use Conversation Memory

```python
from lib.build_rag import build_rag
rag_chain = build_rag(vs, with_memory=True)
```

## 📚 Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern web framework
- **[LangChain](https://langchain.com/)** - LLM application framework
- **[Ollama](https://ollama.com/)** - Local LLM runtime
- **[ChromaDB](https://www.trychroma.com/)** - Vector database
- **[HuggingFace](https://huggingface.co/)** - Embeddings
- **[Sentence Transformers](https://www.sbert.net/)** - Text embeddings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Heshan Ranasinghe**
- GitHub: [@DPHeshanRanasinghe](https://github.com/DPHeshanRanasinghe)

## 🙏 Acknowledgments

- InfoTech College of Business & IT
- LangChain community
- Ollama team

