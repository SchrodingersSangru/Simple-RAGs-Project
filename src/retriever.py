from langchain_core.vectorstores import VectorStoreRetriever
from src.vector_store import load_vector_store

def get_retriever(k: int = 3) -> VectorStoreRetriever:
    """Returns a retriever interface from the loaded vector store."""
    vector_store = load_vector_store()
    return vector_store.as_retriever(search_kwargs={"k": k})