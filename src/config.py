from pathlib import Path

# Project Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
VECTOR_DB_DIR = BASE_DIR / "vector_db"

# Ensure directories exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)

# Local Model Configs
# This downloads and runs a 384-dimensional sentence transformer completely locally via CPU/GPU
LOCAL_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LOCAL_LLM_MODEL = "llama3.1:8b"