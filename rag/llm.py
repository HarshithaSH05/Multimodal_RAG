def generate_response(query, context=None):
    if context:
        prompt = f"""
        Use the following context to answer the question.
        If the answer is not in context, say you don't know.

        Context:
        {context}

        Question:
        {query}
        """
    else:
        prompt = query

    # Call your LLM API here
    response = call_llm(prompt)

    return response
