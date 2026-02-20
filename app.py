import streamlit as st
import time
from rag.retriever import retrieve_documents
from rag.llm import generate_response
from utils.file_loader import load_file

st.set_page_config(page_title="InsightForge AI", page_icon="🤖", layout="wide")

# -------------------------
# Session State
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "documents" not in st.session_state:
    st.session_state.documents = []

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:
    st.title("🧠 InsightForge AI")

    if st.button("➕ New Chat"):
        st.session_state.messages = []

    st.markdown("---")
    st.subheader("📂 Upload Documents")

    uploaded_files = st.file_uploader(
        "Upload files",
        type=["pdf", "txt", "docx", "csv"],
        accept_multiple_files=True
    )

    if uploaded_files:
        for file in uploaded_files:
            content = load_file(file)
            st.session_state.documents.append(content)

        st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")

    st.markdown("---")
    st.info("Multimodal RAG Assistant")

# -------------------------
# Main Chat Area
# -------------------------
st.title("💬 AI Document Chat")

# Display Chat Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------
# User Input
# -------------------------
user_input = st.chat_input("Ask something about your documents...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # AI Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            start_time = time.time()

            retrieved_context = retrieve_documents(user_input)
            response = generate_response(user_input, retrieved_context)

            end_time = time.time()

            st.markdown(response)
            st.caption(f"⏱ Response time: {round(end_time - start_time, 2)} sec")

    st.session_state.messages.append({"role": "assistant", "content": response})
