from transformers import pipeline

# Load model once
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def generate_response(query, context=None):
    if context:
        prompt = f"""
        Use the following context to answer the question.
        If the answer is not in the context, say you don't know.

        Context:
        {context}

        Question:
        {query}
        """
    else:
        prompt = query

    result = generator(prompt, max_length=256)
    return result[0]["generated_text"]
