# Quantum RAG System

A Retrieval-Augmented Generation (RAG) application that enables users to ask questions about quantum computing documents using local Large Language Models (LLMs) powered by Ollama.

## Features

* Document ingestion from PDF and TXT files
* Automatic document chunking
* Semantic embeddings using Sentence Transformers
* FAISS vector database for efficient similarity search
* Local inference using Ollama
* Command Line Interface (CLI)
* Retrieval-Augmented Generation pipeline built with LangChain

---

# Project Structure

```text
Sample RAGs project/
│
├── app.py                     # CLI entry point
├── requirements.txt
├── README.md
│
├── data/
│   └── raw/                   # Place PDF/TXT documents here
│
├── src/
│   ├── utils.py
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── rag_pipeline.py
│   └── generator.py
│
└── vector_db/
    └── faiss_index/           # Generated FAISS index
```

---

# How It Works

1. Documents are loaded from the `data/raw/` directory.
2. Documents are split into smaller chunks.
3. Sentence Transformer embeddings are generated.
4. Embeddings are stored in a FAISS vector database.
5. User queries are converted into embeddings.
6. The most relevant document chunks are retrieved.
7. Retrieved context is sent to an Ollama-hosted LLM.
8. The LLM generates an answer based on the retrieved context.

---

# Tech Stack

* Python 3.10+
* LangChain
* FAISS
* Sentence Transformers
* Hugging Face
* Ollama
* PyPDF
* CLI-based interface

---

# Installation

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd "Sample RAGs project"
```

---

## 2. Create a virtual environment

Using Conda:

```bash
conda create -n quantum-rag python=3.10
conda activate quantum-rag
```

Or using venv:

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download and install Ollama from:

https://ollama.com/download

Verify the installation:

```bash
ollama --version
```

---

## 5. Pull an LLM

Example:

```bash
ollama pull llama3.2:1b
```

or

```bash
ollama pull llama3.2:3b
```

Update `src/generator.py` if using a different model than the default.

---

## 6. Start the Ollama server

```bash
ollama serve
```

---

# Adding Documents

Place your documents inside:

```text
data/raw/
```

Supported formats:

* PDF
* TXT

Example:

```text
data/raw/
├── quantum_intro.pdf
├── distributed_quantum.pdf
└── lecture_notes.txt
```

---

# Running the Project

Start the application:

```bash
python app.py
```

You will see:

```text
Welcome to the Simple RAG Project CLI.

1. Ingest Documents
2. Query the System
3. Exit
```

---

## Step 1 – Ingest Documents

Choose:

```text
1
```

The application will:

* Load all documents
* Split them into chunks
* Generate embeddings
* Build a FAISS index

This step only needs to be run again when new documents are added.

---

## Step 2 – Ask Questions

Choose:

```text
2
```

Example questions:

* What is quantum computing?
* Explain distributed quantum computing.
* What are quantum gates?
* What are the challenges in fault-tolerant quantum computing?
* Summarize the uploaded research papers.

---

# Example Output

```text
Enter your question:

What is quantum computing?

Answer:

Quantum computing is a computational paradigm that uses quantum bits (qubits), which leverage superposition and entanglement to perform certain computations more efficiently than classical computers.
```

---

# Configuration

You can customize:

* Embedding model
* Chunk size
* Chunk overlap
* Retrieval `k` value
* Ollama model
* Prompt template

These settings are typically located within the `src/` modules.

---

# Troubleshooting

## Model not found

```
model '<model-name>' not found (404)
```

Pull the required model:

```bash
ollama pull <model-name>
```

Verify installed models:

```bash
ollama list
```

---

## Ollama not running

Start the server:

```bash
ollama serve
```

---

## Missing dependencies

Install project requirements:

```bash
pip install -r requirements.txt
```

---

## Rebuild the vector database

Delete the existing FAISS index:

```text
vector_db/faiss_index/
```

Then run document ingestion again.

---

# Future Improvements

* Web-based interface (Streamlit or Gradio)
* Chat history and conversational memory
* Hybrid search (keyword + semantic)
* Metadata filtering
* Source citation in responses
* Support for DOCX and Markdown
* API endpoints with FastAPI
* Docker support
* Cloud vector databases (Pinecone, Weaviate, Chroma)

---

# License

This project is intended for educational and research purposes. Feel free to modify and extend it for your own use.

---

# Acknowledgements

* LangChain
* Ollama
* FAISS
* Hugging Face
* Sentence Transformers
