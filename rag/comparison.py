def compare_docs(doc1, doc2):
    set1 = set(doc1.split())
    set2 = set(doc2.split())

    added = set2 - set1
    removed = set1 - set2

    return {
        "Added Content": " ".join(list(added)[:100]),
        "Removed Content": " ".join(list(removed)[:100])
    }
