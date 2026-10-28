import os
import numpy as np
import faiss
from config import Config

INDEX_PATH = os.path.join(Config.INDEX_DIR, "index.faiss")
DATA_PATH = os.path.join(Config.INDEX_DIR, "data.npy")

def save_index(chunks, embeddings):
    if not os.path.exists(Config.INDEX_DIR):
        os.makedirs(Config.INDEX_DIR, exist_ok=True)
    embeddings = np.array(embeddings, dtype=np.float32)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, INDEX_PATH)
    np.save(DATA_PATH, np.array(chunks, dtype=object))

def load_index():
    if not os.path.exists(INDEX_PATH) or not os.path.exists(DATA_PATH):
        return None, None
    index = faiss.read_index(INDEX_PATH)
    chunks = np.load(DATA_PATH, allow_pickle=True)
    return index, chunks
