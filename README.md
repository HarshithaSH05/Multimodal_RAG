# InsightForge AI — Multimodal Knowledge Assistant

InsightForge is an end-to-end Multimodal Retrieval-Augmented Generation (RAG) system that enables intelligent question answering and document analysis over:

Text documents (TXT, PDF)

Images such as charts, diagrams, and screenshots

The system goes beyond basic Q&A by generating summaries, insights, comparisons, and study-friendly outputs, making it useful for students, researchers, and professionals.

The system integrates:

Document retrieval using embeddings + FAISS

Vision-based image understanding

Insight generation using LLMs

A modern Streamlit interface


## Features

• Text-based RAG over TXT and PDF documents
• Multimodal support with image understanding
• Automatic document insights:

Summary

Key points

Risks

Opportunities
• Document comparison to detect changes
• Study Mode for simplified learning summaries
• Vector similarity retrieval using FAISS
• Lightweight reranking for improved relevance
• Guardrails for grounded responses
• Session-based chat memory
• Latency tracking in the UI
• Metadata filtering for selective retrieval


Architecture Overview

User uploads documents or images.

Documents are parsed and chunked.

Images are converted to semantic text using vision models.

Text chunks are embedded into vectors.

FAISS retrieves relevant context.

Results are reranked.

LLM generates grounded answers and insights.


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

