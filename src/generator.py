from langchain_ollama import OllamaLLM
from src.config import LOCAL_LLM_MODEL

def get_llm() -> OllamaLLM:
    """Returns a completely local Ollama LLM instance."""
    return OllamaLLM(
        model=LOCAL_LLM_MODEL,
        temperature=0.0
    )