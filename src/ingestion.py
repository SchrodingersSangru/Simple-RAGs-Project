from pathlib import Path
from typing import List
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document
from src.config import RAW_DATA_DIR

def load_raw_documents() -> List[Document]:
    """Loads all PDF and TXT documents from the raw data directory."""
    documents = []
    
    # Supported extensions
    extensions = ["*.pdf", "*.txt"]
    
    for ext in extensions:
        for file_path in RAW_DATA_DIR.glob(ext):
            print(f"Loading: {file_path.name}")
            try:
                if ext == "*.pdf":
                    loader = PyPDFLoader(str(file_path))
                else:
                    loader = TextLoader(str(file_path), encoding="utf-8")
                
                documents.extend(loader.load())
            except Exception as e:
                print(f"Error loading {file_path.name}: {e}")
                
    print(f"Total document pages/segments loaded: {len(documents)}")
    return documents