# 🚀 Quick Start Guide - AI Engineering Arsenal

## Get Running in 15 Minutes

### Step 1: Clone/Download (1 min)
```bash
# If you have this as a zip, extract it
# If from git, clone it
cd ai-engineering-arsenal
```

### Step 2: Virtual Environment (2 min)
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies (5 min)
```bash
# Install everything
pip install --upgrade pip
pip install -r requirements.txt

# Verify installation
python -c "import anthropic; import openai; import chromadb; print('✓ All imports successful!')"
```

### Step 4: Set Up API Keys (2 min)
```bash
# Copy template
cp .env.example .env

# Edit .env file and add your keys:
# - Get Anthropic key: https://console.anthropic.com/
# - Get OpenAI key: https://platform.openai.com/api-keys
```

Required `.env` content:
```env
ANTHROPIC_API_KEY=sk-ant-xxxxx
OPENAI_API_KEY=sk-xxxxx
```

### Step 5: Test Everything (3 min)
```bash
# Test Claude client
python -c "
from common.llm_clients import ClaudeClient
client = ClaudeClient()
response = client.chat([{'role': 'user', 'content': 'Hi! Say hello in one sentence.'}])
print('Claude says:', response)
"

# Test embeddings
python -c "
from common.llm_clients import OpenAIClient
client = OpenAIClient()
emb = client.get_embedding('test')
print(f'✓ Embedding created: {len(emb)} dimensions')
"

# Test vector store
python -c "
from common.vector_store import ChromaDBStore
store = ChromaDBStore('test')
print(f'✓ ChromaDB initialized, count: {store.get_count()}')
store.delete_collection()
"
```

### Step 6: Choose Your Path (2 min)

**New to AI Engineering?**
→ Start with **Project 1: Knowledge Base**
```bash
cd project-1-knowledge-base
# Read the README
cat README.md
```

**Want to learn by watching first?**
→ Check the YouTube playlist
```bash
cat learning/youtube-playlist.md
```

---

## 🎯 Your First Project in 30 Minutes

### Project 1: Build a Simple Q&A Bot

1. **Add a document** (any PDF or .txt file)
   ```bash
   # Copy a PDF to data folder
   cp ~/Downloads/some-document.pdf project-1-knowledge-base/data/
   ```

2. **Run ingestion**
   ```bash
   cd project-1-knowledge-base
   python src/ingest.py
   ```
   
   You should see:
   ```
   ✓ Ingested X chunks from 1 document(s)
   ```

3. **Test it** (create a simple query script)
   ```bash
   # Create a quick test
   cat > test_query.py << 'EOF'
   import sys
   sys.path.append('..')
   from common.llm_clients import ClaudeClient, OpenAIClient
   from common.vector_store import ChromaDBStore

   # Initialize
   embedding_client = OpenAIClient()
   vector_store = ChromaDBStore('knowledge_base')
   claude = ClaudeClient()

   # Query
   query = "What is this document about?"
   query_emb = embedding_client.get_embedding(query)
   results = vector_store.search(query_emb, top_k=3)

   # Build context
   context = "\n\n".join([r.content for r in results])
   
   # Ask Claude
   prompt = f"""Based on this context, answer the question.

   Context:
   {context}

   Question: {query}
   
   Answer concisely based only on the context provided."""

   answer = claude.chat([{"role": "user", "content": prompt}])
   print(f"\nQuestion: {query}")
   print(f"\nAnswer: {answer}")
   EOF

   python test_query.py
   ```

**Congratulations! You just built your first RAG application! 🎉**

---

## 📚 What Next?

### Learn the Theory (pick one video to start)
1. Watch "RAG Explained in 20 Minutes" 
   - Link in `learning/youtube-playlist.md`

2. Watch "LangChain Master Class For Beginners"
   - Follow along with code

### Improve Your Project
1. Add more documents
2. Try different questions
3. Experiment with chunk sizes
4. Add a Streamlit UI

### Move to Project 2
Once comfortable with Project 1:
```bash
cd ../project-2-code-assistant
cat README.md
```

---

## 🐛 Troubleshooting

**"ModuleNotFoundError: No module named 'anthropic'"**
→ Activate your virtual environment:
```bash
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

**"AuthenticationError: Invalid API key"**
→ Check your `.env` file has correct keys
→ Make sure `.env` is in the root directory

**"No documents found"**
→ Check files are in `project-1-knowledge-base/data/`
→ Supported formats: .pdf, .txt, .md

**Embedding dimension mismatch**
→ Delete the vector DB and re-run:
```bash
rm -rf chroma_db/
python src/ingest.py
```

---

## 💡 Pro Tips

1. **Use tmux/screen** if on remote server
2. **Keep separate terminals** for different processes
3. **Git commit frequently** as you make progress
4. **Document your learnings** in `learning/notes/`
5. **Join communities:**
   - LangChain Discord
   - r/LangChain subreddit
   - Anthropic Discord

---

## 🎓 Learning Resources

**In this repo:**
- `/learning/youtube-playlist.md` - Curated videos
- `/learning/code-snippets/` - Useful patterns
- `/learning/notes/` - Your learning notes

**External:**
- Anthropic Docs: https://docs.anthropic.com/
- LangChain Docs: https://python.langchain.com/
- OpenAI Cookbook: https://cookbook.openai.com/

---

**Ready to build? Start with Project 1!**

```bash
cd project-1-knowledge-base && cat README.md
```
