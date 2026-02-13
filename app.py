import streamlit as st

from utils.pdf_parser import extract_pdf_text
from rag.chunking import chunk_text
from rag.embeddings import embed
from rag.retriever import VectorStore
from rag.llm import generate_answer
from rag.insight_engine import generate_insights
from rag.vision import image_to_text

st.set_page_config(layout="wide")
st.title("InsightForge AI")

uploaded_file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])
uploaded_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

text_data = ""

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        text_data = extract_pdf_text(uploaded_file)
    else:
        text_data = uploaded_file.read().decode("utf-8")

if uploaded_image:
    vision_text = image_to_text(uploaded_image)
    text_data += "\n" + vision_text

if text_data:
    chunks = chunk_text(text_data)
    embeddings = embed(chunks)

    store = VectorStore(embeddings.shape[1])
    store.add(embeddings, chunks)

    query = st.text_input("Ask a question")

    if query:
        q_embed = embed([query])
        results, confidence = store.search(q_embed)

        context = " ".join(results)
        answer = generate_answer(context, query)

        st.subheader("Answer")
        st.write(answer)

        st.write(f"Confidence Score: {confidence:.2f}")

    if st.button("Generate Insights"):
        insights = generate_insights(text_data)
        st.subheader("Insights")
        st.write(insights)
