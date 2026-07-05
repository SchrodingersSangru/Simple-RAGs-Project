import os
from typing import List
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from src.config import VECTOR_DB_DIR
from src.embedding import get_embedding_model

DB_INDEX_PATH = VECTOR_DB_DIR / "faiss_index"

def build_and_save_vector_store(chunks: List[Document]) -> FAISS:
    """Creates a FAISS vector store from document chunks and saves it locally."""
    embeddings = get_embedding_model()
    print("Generating embeddings and building FAISS index...")
    vector_store = FAISS.from_documents(chunks, embeddings)
    
    vector_store.save_local(str(DB_INDEX_PATH))
    print(f"Vector store successfully saved to {DB_INDEX_PATH}")
    return vector_store

def load_vector_store() -> FAISS:
    """Loads an existing local FAISS vector store."""
    embeddings = get_embedding_model()
    if not (DB_INDEX_PATH / "index.faiss").exists():
        raise FileNotFoundError("FAISS index not found. Please ingest documents first.")
    
    return FAISS.load_local(
        str(DB_INDEX_PATH), 
        embeddings, 
        allow_dangerous_deserialization=True  # Required for local FAISS loading
    )