def generate_insights(text):
    return {
        "Summary": text[:300],
        "Key Points": text[:400],
        "Risks": "Potential risk areas identified.",
        "Opportunities": "Possible improvement opportunities detected."
    }
