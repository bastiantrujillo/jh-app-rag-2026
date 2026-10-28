from sentence_transformers import SentenceTransformer
from config import Config

embedder = SentenceTransformer(Config.EMBEDDING_MODEL)

def generate_embeddings(texts):
    if not texts:
        return []
    return embedder.encode(texts, convert_to_numpy=True).tolist()
