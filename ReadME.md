#  InfoTech College Chatbot

A RAG (Retrieval-Augmented Generation) chatbot with a **beautiful web interface** built for InfoTech College of Business & IT.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-orange.svg)

##  Features

-  **Web Chat Interface** - Beautiful, responsive chat UI
-  **RAG Pipeline** - Retrieval-Augmented Generation for accurate responses
-  **FastAPI Backend** - High-performance REST API
-  **Ollama LLM** - Local DeepSeek-r1:1.5b model
-  **ChromaDB** - Vector database for semantic search
-  **Multi-format** - Supports PDF, TXT, and Markdown files

---

##  Quick Start (5 Minutes)

### Prerequisites

1. **Python 3.10+** installed
2. **Ollama** installed from https://ollama.com/download

### Step 1: Clone & Enter Directory

```bash
git clone https://github.com/DPHeshanRanasinghe/ChatBot.git
cd ChatBot
```

### Step 2: Create Virtual Environment

```bash
# Using conda (recommended)
conda create -n chatbot python=3.10 -y
conda activate chatbot

# OR using venv
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Setup Ollama Model

Open a **new terminal** and run:
```bash
ollama pull deepseek-r1:1.5b
ollama serve
```
Keep this terminal running!

### Step 5: Add Your Documents

Place your PDF, TXT, or MD files in the `docs/` folder. These will be the chatbot's knowledge base.

### Step 6: Run the Chatbot

```bash
python -m uvicorn chat_api:app --reload
```

### Step 7: Open the Website! 

Open your browser and go to:

 **http://localhost:8000**

You'll see a beautiful chat interface where you can ask questions!

---

##  Daily Usage (Already Installed)

If you've already set up the project and just want to run it:

### 1. Open Terminal in the ChatBot folder

### 2. Activate your environment
```bash
# If using conda
conda activate chatbot

# If using venv (Windows)
venv\Scripts\activate
```

### 3. Make sure Ollama is running
```bash
ollama serve
```

### 4. Start the server
```bash
python -m uvicorn chat_api:app --reload
```

### 5. Open http://localhost:8000 in your browser

**That's it!** 

---

##  What You'll See

When you open http://localhost:8000, you'll get:

-  **Chat Window** - Type questions and get AI responses
-  **Quick Buttons** - Pre-made questions to try
-  **Input Box** - Type your own questions
-  **AI Assistant** - Answers based on your documents

---

##  Two Ways to Use

| Mode | Command | Access |
|------|---------|--------|
| **Web UI**  | `python -m uvicorn chat_api:app --reload` | http://localhost:8000 |
| **Terminal** | `python main.py` | Type in terminal |
| **API Docs** | (after starting server) | http://localhost:8000/docs |

---

##  Project Structure

```
ChatBot/
├── chat_api.py          # FastAPI REST API
├── main.py              # CLI interface
├── config.py            # Configuration
├── requirements.txt     # Dependencies
├── static/
│   └── index.html       # Web chat interface 
├── lib/                 # Core modules
├── docs/                # Your documents go here 
└── chromadb/            # Vector database (auto-created)
```

---

##  Configuration

Edit `.env` file or `config.py` to customize:

| Setting | Default | Description |
|---------|---------|-------------|
| `LLM_MODEL` | `deepseek-r1:1.5b` | Ollama model |
| `CHUNK_SIZE` | `1000` | Document chunk size |
| `RETRIEVER_K` | `4` | Number of docs to retrieve |

---

##  Troubleshooting

### "Connection refused" error
→ Make sure Ollama is running: `ollama serve`

### "Model not found" error
→ Pull the model: `ollama pull deepseek-r1:1.5b`

### Port already in use
→ Use a different port: `python -m uvicorn chat_api:app --port 8001`

### Slow first response
→ Normal! First time loads the model into memory.

---

##  Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [LangChain](https://langchain.com/) - LLM framework
- [Ollama](https://ollama.com/) - Local LLM
- [ChromaDB](https://www.trychroma.com/) - Vector database
- [HuggingFace](https://huggingface.co/) - Embeddings

---

## Author

**Heshan Ranasinghe**  
Electronic and Telecommunication Engineering Undergraduate

- Email: hranasinghe505@gmail.com
- GitHub: [@DPHeshanRanasinghe](https://github.com/DPHeshanRanasinghe)
- LinkedIn: [Heshan Ranasinghe](https://www.linkedin.com/in/heshan-ranasinghe-988b00290)


---

