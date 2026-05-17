# Project 1: Personal Knowledge Base

## 🎯 Goal
Build a RAG-powered Q&A system over your personal documents (PDFs, articles, notes). Learn the fundamentals of document ingestion, chunking, embeddings, and retrieval.

## 🧠 What You'll Learn
- Document loading and parsing (PDFs, text files)
- Text chunking strategies
- Creating and storing embeddings
- Semantic search with vector databases
- RAG pipeline architecture
- Building a simple UI with Streamlit

## 🏗️ Architecture

```
User Query
    ↓
[Embedding Model] → Query Vector
    ↓
[Vector DB Search] → Retrieve Top K Chunks
    ↓
[LLM (Claude)] ← Augmented Prompt (Query + Context)
    ↓
Generated Answer (with citations)
```

## 📁 Project Structure

```
project-1-knowledge-base/
├── data/                   # Drop your PDFs here
│   └── .gitkeep
├── notebooks/
│   └── 01_explore_rag.ipynb    # Jupyter experiments
├── src/
│   ├── __init__.py
│   ├── ingest.py          # Document ingestion pipeline
│   ├── query.py           # RAG query engine
│   └── app.py             # Streamlit UI
├── tests/
│   └── test_ingest.py
└── README.md              # This file
```

## 🚀 Quick Start

### 1. Add Your Documents
```bash
# Copy PDFs/text files to the data folder
cp ~/Downloads/*.pdf data/
```

### 2. Run Ingestion
```bash
# Process documents and build vector index
python src/ingest.py
```

This will:
- Load all documents from `data/`
- Split them into chunks (default: 1000 chars, 200 overlap)
- Create embeddings using OpenAI
- Store in ChromaDB

### 3. Test Queries
```bash
# Try a query from command line
python src/query.py "What are the main topics in my documents?"
```

### 4. Launch UI
```bash
# Start Streamlit app
streamlit run src/app.py
```

## 🔧 Configuration

Edit settings in `.env`:
```env
CHUNK_SIZE=1000          # Characters per chunk
CHUNK_OVERLAP=200        # Overlap between chunks
TOP_K_RESULTS=5          # Number of chunks to retrieve
```

## 💡 Usage Examples

**Basic Query:**
```python
from src.query import KnowledgeBase

kb = KnowledgeBase()
answer = kb.query("What is machine learning?")
print(answer)
```

**With Citations:**
```python
answer, sources = kb.query_with_sources("Explain RAG")
print(f"Answer: {answer}\n")
print("Sources:")
for source in sources:
    print(f"  - {source['metadata']['source']}")
```

## 🧪 Experiments to Try

1. **Different Chunk Sizes**
   - Try 500, 1000, 2000 character chunks
   - Observe impact on answer quality

2. **Hybrid Search**
   - Combine vector search with keyword (BM25)
   - See when each performs better

3. **Re-ranking**
   - Retrieve top 10, re-rank to top 3
   - Use a cross-encoder for better relevance

4. **Different Embeddings**
   - Try `text-embedding-3-large` (more expensive, better quality)
   - Compare local models (sentence-transformers)

## 📊 Evaluation

Test your RAG system:
```bash
python tests/test_ingest.py
```

Manual evaluation checklist:
- [ ] Does it answer questions accurately?
- [ ] Are citations correct?
- [ ] Does it say "I don't know" when appropriate?
- [ ] Response time < 3 seconds?

## 🐛 Common Issues

**Issue:** "No documents found"
- **Fix:** Make sure PDFs are in `data/` folder

**Issue:** "Embedding dimension mismatch"
- **Fix:** Delete `chroma_db/` and re-run ingestion

**Issue:** "API key not found"
- **Fix:** Copy `.env.example` to `.env` and add keys

## 📚 Next Steps

Once this works:
1. Add more document types (Word, HTML, Markdown)
2. Implement conversation memory
3. Add filtering by metadata (date, source, topic)
4. Deploy to Streamlit Cloud

## 🎥 Recommended Videos

Watch these after building:
1. "RAG Explained in 20 Minutes" - Understand theory
2. "Local RAG from Scratch" - See low-level implementation
3. "Complete RAG Tutorial 2026" - Learn advanced patterns

---

**Stuck? Check `learning/notes/` for troubleshooting tips!**
