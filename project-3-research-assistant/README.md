# Project 3: Automated Research Assistant

## 🎯 Goal
Build an AI research agent that can search the web, synthesize information from multiple sources, and generate comprehensive reports. Learn MCP (Model Context Protocol) for tool integration.

## 🧠 What You'll Learn
- MCP server integration
- Multi-step agent workflows
- Web search and data synthesis
- Report generation
- Agentic AI patterns
- Tool calling with Claude

## 🏗️ Architecture

```
User Research Query
    ↓
[Planning Agent] → Break down into sub-questions
    ↓
[Search Agent] → Execute searches (MCP web search)
    ↓
[Extraction Agent] → Pull key information
    ↓
[Synthesis Agent] → Combine findings
    ↓
[Report Generator] → Structured markdown report
    ↓
Saved to outputs/
```

## 📁 Project Structure

```
project-3-research-assistant/
├── outputs/                # Generated reports
│   └── .gitkeep
├── notebooks/
│   └── 03_agent_experiments.ipynb
├── src/
│   ├── __init__.py
│   ├── search_agent.py     # MCP-powered search
│   ├── synthesizer.py      # Multi-source synthesis
│   └── app.py              # Main interface
└── README.md
```

## 🚀 Quick Start

### 1. Set Up MCP Search Tool
```bash
# Install MCP server for Brave Search
npm install -g @modelcontextprotocol/server-brave-search

# Or use built-in search APIs (Tavily, DuckDuckGo)
# Configure in .env:
# TAVILY_API_KEY=your_key
```

### 2. Run Research
```bash
python src/search_agent.py "What are the latest developments in quantum computing?"
```

### 3. Generate Report
```bash
# Creates a markdown report in outputs/
python src/synthesizer.py --query "Compare React vs Vue in 2026" --depth comprehensive
```

### 4. Interactive UI
```bash
streamlit run src/app.py
```

## 🔧 Features

- **Multi-step research** (iterative query refinement)
- **Source diversification** (multiple search queries)
- **Fact verification** (cross-reference sources)
- **Structured outputs** (markdown reports with citations)
- **Cost tracking** (monitor API usage)
- **Resume capability** (continue interrupted research)

## 💡 Example Research Topics

- "Compare AI frameworks for production deployment"
- "Latest research on RAG architectures"
- "How are companies using Claude API in 2026?"
- "Security best practices for LLM applications"
- "Performance benchmarks: Claude vs GPT-4"

## 🧪 Agent Patterns to Implement

1. **ReAct Pattern** (Reasoning + Acting)
   - Think → Act → Observe → Repeat

2. **Tree of Thoughts**
   - Explore multiple research paths
   - Choose best branch

3. **Chain of Verification**
   - Generate answer
   - Generate verification questions
   - Re-search and verify

4. **Multi-Agent Collaboration**
   - Search specialist
   - Technical analyst
   - Report writer

## 📊 MCP Tools to Integrate

**Built-in:**
- `web_search` - General web search
- `web_fetch` - Fetch specific URLs

**External MCP Servers:**
- `@modelcontextprotocol/server-brave-search` - Search
- `@modelcontextprotocol/server-filesystem` - Save reports
- `@modelcontextprotocol/server-github` - Code research
- Custom MCP servers (build your own!)

## 🎥 Recommended Videos & Courses

**Must Complete:**
1. Anthropic Academy: "Introduction to MCP"
2. Anthropic Academy: "MCP: Advanced Topics"
3. "LangChain Mastery" - Agents chapter

**Helpful:**
- "Tips for building AI agents" (Anthropic)
- "Lessons on AI agents from Claude Plays Pokemon"

## 📚 Advanced Features to Add

1. **Memory System**
   - Remember previous research
   - Build knowledge graph

2. **Multi-Modal**
   - Include images, charts
   - Process PDFs from web

3. **Collaborative Research**
   - Share research workspace
   - Team annotations

4. **Automated Scheduling**
   - Monitor topics over time
   - Email digest of updates

## 🐛 Common Challenges

**Challenge:** Too many API calls
- **Solution:** Implement caching, batch requests

**Challenge:** Inconsistent outputs
- **Solution:** Use structured outputs, validation

**Challenge:** Missing sources
- **Solution:** Maintain source tracking throughout pipeline

**Challenge:** Hallucination
- **Solution:** Verify claims, quote sources directly

## 📈 Evaluation Metrics

- ✅ Source diversity (>3 unique domains)
- ✅ Claim verification (all claims cited)
- ✅ Comprehensiveness (covers all aspects)
- ✅ Freshness (prefers recent sources)
- ✅ Cost efficiency (<$0.50 per report)

## 🚀 Deployment Ideas

- **Slack bot** - "/research [topic]"
- **Scheduled reports** - Daily AI news digest
- **API service** - Research-as-a-service
- **Browser extension** - Right-click research

---

**This is the capstone project - complete Projects 1 & 2 first!**
**Watch Anthropic MCP courses before starting.**
