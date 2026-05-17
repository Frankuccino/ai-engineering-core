# Project 2: Code Documentation Assistant

## 🎯 Goal
Build an AI assistant that understands codebases. Point it at any GitHub repo and ask questions about how the code works, architecture decisions, or find specific implementations.

## 🧠 What You'll Learn
- Code parsing with tree-sitter
- Semantic code search
- Working with git repositories
- Code-specific embeddings
- Multi-file context management

## 🏗️ Architecture

```
GitHub Repo
    ↓
[Code Parser] → Extract functions, classes, comments
    ↓
[Chunking Strategy] → Smart code chunking (preserve context)
    ↓
[Embeddings] → Code-aware embeddings
    ↓
[Vector DB] → Indexed codebase
    ↓
User Query → Retrieve relevant code → Claude generates explanation
```

## 📁 Project Structure

```
project-2-code-assistant/
├── repos/              # Clone repos here
│   └── .gitkeep
├── notebooks/
│   └── 02_code_exploration.ipynb
├── src/
│   ├── __init__.py
│   ├── repo_indexer.py       # Clone & parse repos
│   ├── semantic_search.py    # Code search engine
│   └── app.py                # Query interface
└── README.md
```

## 🚀 Quick Start

### 1. Index a Repository
```bash
# Clone and index a repo
python src/repo_indexer.py https://github.com/username/repo-name
```

### 2. Ask Questions
```bash
python src/semantic_search.py "How does authentication work in this codebase?"
```

### 3. Or Use the UI
```bash
streamlit run src/app.py
```

## 🔧 Features

- **Automatic repo cloning**
- **Language detection** (Python, JavaScript, TypeScript, etc.)
- **Smart chunking** (preserves function/class boundaries)
- **Code-aware search** (understands syntax, not just text)
- **Multi-file context** (shows related files)
- **Git history integration** (when was code written?)

## 💡 Example Questions

- "How is user authentication implemented?"
- "Show me all database query functions"
- "What libraries are used for API requests?"
- "Find the function that handles file uploads"
- "Explain the architecture of this service"
- "Where is error handling done?"

## 🧪 Experiments to Try

1. **Compare Different Repos**
   - Index multiple repos
   - Ask same question across all
   - See different implementation patterns

2. **Code Review Assistant**
   - Ask about potential issues
   - Security vulnerabilities
   - Performance bottlenecks

3. **Learning Tool**
   - Index popular open-source projects
   - Learn design patterns
   - Understand best practices

## 📊 What Gets Indexed

- ✅ Function definitions with docstrings
- ✅ Class definitions
- ✅ Important comments
- ✅ File-level documentation
- ✅ README and docs
- ❌ Test files (optional)
- ❌ Node_modules, venv, etc.

## 🎥 Recommended Videos

Watch after building Project 1:
1. "Hands-On RAG with LangChain" - Apply to code
2. "LangChain Mastery" - Advanced retrieval patterns

## 📚 Next Steps

1. Add support for more languages (Rust, Go, Java)
2. Integrate with IDE (VS Code extension)
3. Add chat memory (conversational debugging)
4. Compare codebases (migration planning)

---

**Build this after completing Project 1!**
