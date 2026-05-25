# AI Engineering Core

## My Implementation Blueprint & AI-Native Architecture

This repository contains my direct, hands-on implementations of modern AI engineering paradigms. It serves as my active execution ground for building intelligent microservices, mastering LLM orchestration, and developing deep technical capabilities in AI-native software architecture.

> 🔗 **Blueprint & Roadmap Reference**  
> This codebase is the direct concrete execution of the system architectures and technical roadmaps designed in my foundational repository: **[Frankuccino/ai-engineering-arsenal](https://github.com/Frankuccino/ai-engineering-arsenal)**

### 📁 Project Structure

```text
ai-engineering-arsenal/
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignore patterns
├── requirements.txt                # All dependencies
├── README.md                       # This file
│
├── common/                         # Shared utilities
│   ├── __init__.py
│   ├── llm_clients.py             # Anthropic & OpenAI clients
│   ├── embeddings.py              # Embedding utilities
│   ├── vector_store.py            # Vector DB wrappers
│   └── utils.py                   # Helper functions
│
├── project-1-knowledge-base/       # Personal Knowledge Base
│   ├── README.md                  # Project-specific docs
│   ├── data/                      # Your PDFs/documents
│   ├── notebooks/                 # Jupyter experiments
│   ├── src/
│   │   ├── ingest.py             # Document processing
│   │   ├── query.py              # RAG query engine
│   │   └── app.py                # Streamlit UI
│   └── tests/                    # Unit tests
│
├── project-2-code-assistant/      # Code Documentation Assistant
│   ├── README.md
│   ├── repos/                    # Clone repos here
│   ├── notebooks/
│   ├── src/
│   │   ├── repo_indexer.py      # Code parsing & indexing
│   │   ├── semantic_search.py   # Search implementation
│   │   └── app.py               # Query interface
│   └── tests/
│
├── project-3-research-assistant/  # Automated Research Assistant
│   ├── README.md
│   ├── outputs/                  # Generated reports
│   ├── notebooks/
│   ├── src/
│   │   ├── search_agent.py      # MCP-powered search
│   │   ├── synthesizer.py       # Multi-source synthesis
│   │   └── app.py               # Main interface
│   └── tests/
│
└── learning/                      # Learning resources
    ├── youtube-playlist.md        # Curated video list
    ├── code-snippets/            # Useful patterns
    └── notes/                    # Your learning notes
```

## 🚀 **Execution Environment**

To reproduce my development environment and run these subsystems locally:

1. Environment Initialization

```bash
# Create isolated Python runtime
python -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
	venv\Scripts\activate

# Install consolidated system dependencies
pip install -r requirements.txt
```

2. Secrets & Configurations

```bash
# Clone the environment template
cp .env.example .env

# Required API keys for core functionality:
# - ANTHROPIC_API_KEY (Primary LLM orchestration)
# - OPENAI_API_KEY (Vector embeddings)

```

---

### 🎯 **My 2026 Engineering Objectives**

This repository tracks my strategic objective to achieve comprehensive AI-native awareness and production-grade capabilities this year. My execution roadmap is broken into three phases:

1. **Phase I (Knowledge Base)**: Engineering deterministic RAG pipelines, managing context windows, and mastering chunking strategies.

2. **Phase II (Code Assistant)**: Moving beyond basic text retrieval into semantic AST (Abstract Syntax Tree) code parsing and dependency-aware vector embeddings.

3. **Phase III (Research Assistant)**: Implementing autonomous agent loops and programmatic tool execution using the Model Context Protocol (MCP).

---

### 🏆 **Core Capabilities Engineered**

Through these implementations, I am establishing a permanent toolkit for:

- ✅ **Production RAG Architectures**: Designing resilient data ingestion and retrieval systems.

- ✅ **Vector Infrastructures**: Managing highly dimensional data within ChromaDB, Qdrant, and Pinecone.

- ✅ **Agentic Systems**: Orchestrating multi-step, autonomous programmatic behaviors.

- ✅ **LLM Orchestration**: Handling API abstraction, rate-limiting, and structured outputs natively.

- ✅ **Model Context Protocol (MCP)**: Implementing MCP to seamlessly bridge frontier LLMs with local tools, filesystems, and external execution runtimes.

---

# 🧱 The Missing 10%–15% — The Path to Elite Architecture Mastery

While executing Phases I, II, and III establishes solid mid-to-senior level competency (~85%–90%), bridging the gap toward becoming a completely independent, elite AI Systems Architect requires diving into advanced, production-hardened optimization vectors.

I am using this codebase to actively explore and implement the following mechanics:

---

## 1. Production Telemetry & Guardrails (+5%)

### The Challenge

Building an agent is easy; keeping an agent from going off the rails in production is hard. Non-deterministic models require deterministic runtime guardrails.

### Action Plan

Integrating a strict validation layer within:

- `src/search_agent.py`
- `src/synthesizer.py`

I am building self-correction loops that force the model to cross-examine its outputs against retrieved source contexts before serving responses. Additionally, I am implementing prompt injection mitigation using semantic guardrails such as Llama Guard.

---

## 2. Cost & Latency Optimization (+5%)

### The Challenge

In enterprise production environments, sequential LLM calls are a death sentence for user experience.

### Action Plan

Implementing a specialized Semantic Cache engine within:

- `common/vector_store.py`

Before invoking a frontier LLM, the system checks the vector database for highly similar historical queries (>0.95 cosine similarity). If a match is found, the response is served instantly, bypassing unnecessary LLM processing overhead.

Additionally:

- `common/llm_clients.py` orchestrates parallel tool-calling workflows
- API-level prompt caching is leveraged for heavy contextual payloads

---

## 3. Evaluation Rigor (+5%)

### The Challenge

Generic framework scores are insufficient for business-specific reliability. True evaluation requires domain-specific benchmarking datasets.

### Action Plan

Building custom deterministic Ground Truth evaluation datasets inside:

- `tests/`

Rather than simply verifying successful application execution, the `pytest` pipelines process live outputs against static, known ground-truth pairs to produce measurable metrics for:

- Faithfulness
- Context Recall
- Answer Relevance

Evaluation workflows leverage:

- RAGAS
- LangSmith tracking

---

### 🛠️ **Core Tech Stack**

- **Intelligence**: Claude 3.5 Sonnet (Anthropic API), GPT-4o (OpenAI API)

- **Frameworks**: LangChain, LlamaIndex

- **Vector** Infrastructures: ChromaDB, Qdrant, Pinecone

- **Document & Code Parsing**: pypdf, unstructured, tree-sitter, Pygments, GitPython

- **System Observability**: LangSmith, RAGAS (Automated retrieval scoring)

- **Interfaces**: FastAPI, Streamlit, Gradio

### 🧠 **Engineering Principles & Iteration**

My focus when building these systems is on conceptual clarity and high-performance execution.

1. **Unified Infrastructure**: I keep API wrappers and vector store connections in the common/ module to enforce DRY principles across all subsystems.

2. **Experimentation First**: notebooks/ directories are used heavily to trace similarity thresholds and chunking logic before committing to the main application pipeline.

3. **Strict Validation**: Ensuring every subsystem is tested deterministically (python -m pytest) to map the boundaries of non-deterministic LLM outputs.
