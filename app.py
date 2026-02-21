import streamlit as st
import time
import numpy as np

# ✅ FIXED IMPORTS (absolute package imports for Streamlit Cloud)
from multimodal_rag.rag.retriever import retrieve_documents, vector_store, embedder
from multimodal_rag.rag.llm import generate_response
from multimodal_rag.utils.file_loader import load_file


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="InsightForge AI",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.title("🚀 InsightForge AI")
    st.caption("ChatGPT-style AI + RAG")

    st.markdown("---")

    uploaded_files = st.file_uploader(
        "Upload Documents",
        type=["pdf", "txt", "docx", "csv"],
        accept_multiple_files=True
    )

    # ADD DOCUMENTS TO VECTOR STORE
    if uploaded_files:
        for file in uploaded_files:
            content = load_file(file)

            chunks = [content]

            embeddings = embedder.encode(chunks).astype("float32")
            vector_store.add(embeddings, chunks)

        st.success(f"{len(uploaded_files)} document(s) uploaded & indexed")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# --------------------------------------------------
# MAIN CHAT UI
# --------------------------------------------------
st.title("💬 AI Chat Assistant")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------
user_input = st.chat_input("Ask anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            start_time = time.time()

            if vector_store.index.ntotal > 0:
                context = retrieve_documents(user_input)
                response = generate_response(user_input, context)
            else:
                response = generate_response(user_input, context=None)

            latency = round(time.time() - start_time, 2)

            placeholder = st.empty()
            full_response = ""

            for word in response.split():
                full_response += word + " "
                time.sleep(0.02)
                placeholder.markdown(full_response)

            st.caption(f"⏱ {latency}s")

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
