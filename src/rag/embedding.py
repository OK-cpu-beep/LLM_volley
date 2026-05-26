"""
Embedding model wrapper using sentence-transformers.
"""

from sentence_transformers import SentenceTransformer

# Use a small, fast model suitable for CPU
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

class EmbeddingModel:
    _instance = None
    
    @