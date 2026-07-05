from src.ingestion import load_raw_documents
from src.chunking import chunk_documents
from src.vector_store import build_and_save_vector_store
from src.rag_pipeline import create_rag_chain

def run_ingestion_pipeline():
    """Helper to run the full text parsing and embedding generation lifecycle."""
    print("--- Starting Document Ingestion ---")
    raw_docs = load_raw_documents()
    if not raw_docs:
        print("No documents found in data/raw/. Please add PDF or TXT files.")
        return
    
    chunks = chunk_documents(raw_docs)
    build_and_save_vector_store(chunks)
    print("--- Ingestion Pipeline Finished Successfully ---\n")

def query_rag_system(query: str) -> str:
    """Helper to spin up the chain and answer a single query."""
    chain = create_rag_chain()
    response = chain.invoke({"input": query})
    return response.get("answer", "No answer generated.")