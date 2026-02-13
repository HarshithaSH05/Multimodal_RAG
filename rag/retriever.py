import faiss

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embeddings, texts):
        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, q_embed, k=5):
        D, I = self.index.search(q_embed, k)
        results = [self.texts[i] for i in I[0]]
        confidence = float(1 / (1 + D[0][0]))
        return results, confidence
