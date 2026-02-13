def rerank(chunks, query):
    ranked = sorted(chunks, key=lambda x: query.lower() in x.lower(), reverse=True)
    return ranked
