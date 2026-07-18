## RAG Chat with PDF

### What it does
Upload any PDF and ask questions about it in natural language.
The system retrieves relevant sections and answers accurately.

### Architecture
PDF → PyPDF Loader → Text Splitter → ChromaDB (vector store)
Question → Embedding → Similarity Search → Context + LLM → Answer

### Tech Stack
- LangChain
- ChromaDB (local vector database)
- Sentence Transformers (embeddings)
- Groq API (LLaMA 3)
- Python

### How to run
1. pip install -r requirements.txt
2. Add your PDF to docs/ folder
3. Run create_vectordb.py first
4. Run rag_pipeline.py to chat