def generate_flashcards(text):
    sentences = text.split(".")
    return [f"Q: Explain -> {s.strip()} ?" for s in sentences[:5]]

def generate_quiz(text):
    sentences = text.split(".")
    return [f"What is meant by: {s.strip()} ?" for s in sentences[:5]]
