# About

A powerful document-based chatbot built with Python, FastAPI, and RAG (Retrieval-Augmented Generation) technology. This application combines LangChain, ChromaDB, and Olama's DeepSeq R1 model to create an intelligent chatbot that can understand and respond to queries based on your document collection.

## Key Highlights

🤖 **Smart Document Processing** - Supports PDF, TXT, and Markdown files  
🔍 **Vector Search** - ChromaDB integration for efficient document retrieval  
⚡ **Fast API** - Built on FastAPI for high-performance REST endpoints  
🧠 **Advanced AI** - Powered by Olama DeepSeq R1 1.5b model  
📚 **RAG Technology** - Combines retrieval and generation for accurate responses  

Perfect for building knowledge bases, document Q&A systems, or custom AI assistants that work with your specific content.

# Chatbot using Python and FastAPI

This repository contains a chatbot application built using Python with several advanced libraries and tools, including LangChain, FastAPI, Olama, ChromaDB, HuggingFace, and more. It allows for interacting with a document-based RAG (Retrieval-Augmented Generation) system.

## Features

* **FastAPI Backend:** Utilizes FastAPI for serving the chatbot API.
* **LangChain Integration:** Leverages LangChain for document processing and RAG model building.
* **Olama Model Integration:** DeepSeq r1:1.5b model from Olama for natural language understanding and generation.
* **ChromaDB:** For storing and retrieving documents in a vectorized format, enabling efficient search.
* **PDF, .txt, and .md File Parsing:** Supports parsing and working with PDF, .txt, and .md files.
* **Customizable Chatbot:** Modify or extend chatbot behavior easily using custom document stores and models.

## Installation

### Prerequisites

Ensure you have Conda installed and set up on your machine. You will also need Python 3.7+ to run the application.

### Step 1: Clone the Repository

```bash
git clone https://github.com/DPHeshanRanasinghe/ChatBot.git
cd ChatBot
```

### Step 2: Set Up Conda Environment

```bash
conda create -n chatbot python=3.10 anaconda
conda activate chatbot
```

### Step 3: Install Dependencies

Use the provided `requirements.txt` to install the necessary libraries:

```bash
pip install -r requirements.txt
```

Dependencies include:
* **FastAPI**
* **Uvicorn**
* **LangChain**
* **Olama**
* **Chroma**
* **HuggingFace**
* **SentenceTransformers**
* **ChromaDB**
* **PyPDF**

If there's any other specific setup, you can mention it here.

### Step 4: Set Up Olama

To use the Olama DeepSeq r1:1.5b model, you can follow the steps outlined in their documentation. Ensure that you have pulled the correct model and integrated it into the application by referencing the model in your configuration file.

### Step 5: Run the Application

Once you have installed all dependencies and set up the environment, you can start the FastAPI application with:

