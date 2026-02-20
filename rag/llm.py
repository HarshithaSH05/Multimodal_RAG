from transformers import pipeline

# Use text-generation instead of text2text-generation
generator = pipeline(
    "text-generation",
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
Answer:
"""
    else:
        prompt = query

    result = generator(
        prompt,
        max_length=256,
        do_sample=True,
        temperature=0.7
    )

    return result[0]["generated_text"]
