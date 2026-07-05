from langchain_huggingface import HuggingFaceEmbeddings
from src.config import LOCAL_EMBEDDING_MODEL

def get_embedding_model() -> HuggingFaceEmbeddings:
    """Returns a completely local Hugging Face embedding model interface."""
    model_kwargs = {'device': 'cpu'}  # Change to 'cuda' if you have an Nvidia GPU
    encode_kwargs = {'normalize_embeddings': True}
    
    return HuggingFaceEmbeddings(
        model_name=LOCAL_EMBEDDING_MODEL,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )