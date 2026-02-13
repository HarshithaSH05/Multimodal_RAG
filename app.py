import streamlit as st
from utils.pdf_parser import extract_pdf_text
from utils.file_loader import load_text
from rag.chunking import chunk_text
from rag.embeddings import embed
from rag.retriever import VectorStore
from rag.reranker import rerank
from rag.llm import generate_answer
from rag.insight_engine import generate_insights
from rag.comparison import compare_docs
from rag.study_mode import generate_flashcards, generate_quiz
from rag.vision import image_to_text
from memory.chat_memory import ChatMemory

st.set_page_config(layout="wide")
st.title("InsightForge AI Assistant")

memory = ChatMemory()

file = st.file_uploader("Upload document", type=["pdf", "txt"])
image = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

text_data = ""

if file:
    if file.name.endswith(".pdf"):
        text_data = extract_pdf_text(file)
    else:
        text_data = load_text(file)

if image:
    vision_text = image_to_text(image)
    text_data += "\n" + vision_text

if text_data:
    chunks = chunk_text(text_data)
    embeddings = embed(chunks)

    store = VectorStore(embeddings.shape[1])
    store.add(embeddings, chunks)

    query = st.text_input("Ask question")

    if query:
        q_embed = embed([query])
        results, conf = store.search(q_embed)
        ranked = rerank(results, query)

        answer = generate_answer(" ".join(ranked), query)
        memory.add(query, answer)

        st.subheader("Answer")
        st.write(answer)
        st.write(f"Confidence Score: {conf:.2f}")

    if st.button("Generate Insights"):
        insights = generate_insights(text_data)
        st.write(insights)

    if st.button("Study Mode"):
        st.subheader("Flashcards")
        st.write(generate_flashcards(text_data))
        st.subheader("Quiz")
        st.write(generate_quiz(text_data))

st.subheader("Recent Chat")
st.write(memory.get())
