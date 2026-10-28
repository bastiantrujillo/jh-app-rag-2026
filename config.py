import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))
    TOP_K = int(os.getenv("TOP_K", 4))
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    LLM_ENDPOINT = os.getenv("LLM_ENDPOINT", "http://127.0.0.1:8080/v1")
    LLM_CHAT_ENDPOINT = os.getenv("LLM_CHAT_ENDPOINT", "/chat/completions")
    INDEX_DIR = os.getenv("INDEX_DIR", "app/data/index")
    PDFS_DIR = os.getenv("PDFS_DIR", "app/data/pdfs")
