# InsightForge AI — Multimodal Knowledge Assistant

InsightForge AI is a **Multimodal Retrieval-Augmented Generation (RAG)** system that enables intelligent question answering and knowledge extraction from **documents and images**.

Beyond standard RAG, the system also generates insights, comparisons, and study materials, acting as a smart knowledge assistant for enterprise and academic use cases.


## Features

- Multimodal document Q&A (PDF, TXT, images)
- Insight generation and summaries
- Document comparison mode
- Study mode (flashcards & quizzes)
- Image understanding for charts and diagrams
- Retrieval reranking for better relevance
- Confidence scoring
- Chat memory for conversational context


## System Flow

1. Documents and images are uploaded.
2. Text is extracted and chunked.
3. Images are converted into semantic text.
4. Content is embedded and stored in FAISS.
5. Relevant chunks are retrieved and reranked.
6. Grounded answers and insights are generated.


## Tech Stack

- Python
- Streamlit
- FAISS Vector Search
- Sentence Transformers Embeddings
- PyPDF
- NumPy


## Project Structure
insightforge/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── rag/
│   ├── __init__.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── reranker.py
│   ├── llm.py
│   ├── vision.py
│   ├── insight_engine.py
│   ├── comparison.py
│   └── study_mode.py
│
├── memory/
│   └── chat_memory.py
│
└── utils/
    ├── pdf_parser.py
    ├── file_loader.py
    └── helpers.py

