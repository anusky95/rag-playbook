# 💼 Case Studies - RAG in the Real World

Theory only takes you so far. This folder applies everything from earlier sections to three concrete, realistic RAG applications.

## 🎯 What You'll Build

Each notebook is a self-contained project you can adapt for your own use:
- A Q&A bot that answers questions over your own documents
- A semantic document search engine
- A code assistant that understands your codebase

## 📚 Notebooks

1. **`00_QA_Bot.ipynb`** ⭐ MOST POPULAR
   - Build a question-answering chatbot over your own text documents
   - Chunking strategy: paragraph-level with overlap
   - Indexing pipeline: load → chunk → embed → store
   - Grounded answers with source citations
   - Handles follow-up questions with conversation history
   - Drop-in for: internal wikis, product docs, support knowledge bases

2. **`01_Document_Search.ipynb`** 🔍
   - Semantic document search: find documents by *meaning*, not keywords
   - Side-by-side comparison of keyword search vs semantic search
   - Embedding title + body together for richer signal
   - Metadata filtering (date range, author, category)
   - Re-ranking results with a cross-encoder
   - Drop-in for: enterprise search, research paper search, content discovery

3. **`02_Code_Assistant.ipynb`** 💻
   - RAG over a codebase: answer questions about how code works
   - Chunking strategy: by function and class (not arbitrary character windows)
   - Metadata: file path, line numbers, language, docstring
   - Answers "How do I use `X`?" and "Where is `Y` implemented?"
   - Drop-in for: developer tooling, onboarding, code review assistance

## 🚀 Quick Start

```python
# Q&A Bot — 5 lines to get started
from qa_bot import QABot

bot = QABot()
bot.index_directory("./my_docs/")  # chunks, embeds, stores
answer = bot.ask("What is the refund policy?")
print(answer.text, answer.sources)

# Document Search
from doc_search import DocumentSearchEngine

engine = DocumentSearchEngine()
engine.index(documents)
results = engine.search("quarterly revenue growth", top_k=10)

# Code Assistant
from code_assistant import CodeAssistant

assistant = CodeAssistant()
assistant.index_repo("./src/")
answer = assistant.ask("How does the authentication middleware work?")
```

## 📊 Case Study Comparison

| Case Study | Chunk Strategy | Key Challenge | Key Technique |
|------------|---------------|---------------|---------------|
| **Q&A Bot** | Paragraph + overlap | Multi-doc synthesis | Citations, conversation history |
| **Doc Search** | Full document | Relevance ranking | Title+body embedding, reranking |
| **Code Assistant** | Function/class | Structural awareness | AST-based chunking, line metadata |

## 💡 Lessons Learned

### Q&A Bot
- Overlap between chunks prevents answer truncation at boundaries
- Conversation history degrades retrieval — reformulate queries before retrieval

### Document Search
- Embedding title + body in a single chunk outperforms title-only or body-only
- Re-ranking adds significant quality at modest latency cost

### Code Assistant
- Character-window chunking breaks functions — always chunk at code boundaries
- Include file path and function signature in the metadata for citations

## 📖 Learning Path

**Beginner → Practitioner:**
1. `00_QA_Bot.ipynb` — the most general and transferable pattern
2. Adapt it to your own documents

**Building a search product:**
1. `01_Document_Search.ipynb`
2. Add filters from `3_search_techniques/05_Routing_and_Filtering.ipynb`

**Developer tooling:**
1. `02_Code_Assistant.ipynb`
2. Extend with `5_advanced_rag/01_Agentic_RAG.ipynb` for multi-step code queries

## 🎓 Production Checklist

- [ ] Chunking strategy matches document structure (not just character windows)
- [ ] Metadata (source, date, section) stored alongside each chunk
- [ ] Citations shown in every answer
- [ ] Conversation history handled correctly (multi-turn Q&A bot)
- [ ] Cold-start tested (no documents indexed)
- [ ] Edge cases from `4_generation/04_Handling_Edge_Cases.ipynb` covered

## 🔗 What's Next?

- **`9_industry_verticals/`** — domain-specific compliance requirements (legal, medical, finance)
- **`7_deployment/`** — wrap any of these into a production API
- **`6_evaluation/`** — measure quality on your specific use case

## 🔧 Installation

```bash
pip install sentence-transformers rank-bm25 anthropic tree-sitter
```

## 🤝 Contributing

Have a case study to add? Open a PR!

---

**Remember:** Every RAG application is unique — adapt the chunking and prompting to your specific document type! 💼
