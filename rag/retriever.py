import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model once
embedder = SentenceTransformer("all-MiniLM-L6-v2")

class VectorStore:
    def __init__(self, dim=384):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embeddings, texts):
        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, q_embed, k=5):
        D, I = self.index.search(q_embed, k)
        results = [self.texts[i] for i in I[0] if i < len(self.texts)]
        confidence = float(1 / (1 + D[0][0]))
        return results, confidence


# Global vector store
vector_store = VectorStore()

def retrieve_documents(query):
    if len(vector_store.texts) == 0:
        return ""

    query_embedding = embedder.encode([query]).astype("float32")
    results, confidence = vector_store.search(query_embedding)

    return " ".join(results)
