# 🎓 Tutorials & Workshops - Build RAG From Scratch

This is the capstone of the ULTIMATE RAG course. Everything you've learned — chunking, embedding, retrieval, reranking, prompting, evaluation — comes together in one complete, production-ready implementation.

## 🎯 What You'll Build

A fully functional `RAGSystem` class that you can drop into any project:
- Ingests documents, chunks them intelligently
- Embeds and indexes chunks
- Retrieves with hybrid search
- Reranks with a CrossEncoder
- Prompts an LLM with retrieved context
- Returns grounded, cited answers

## 📚 Notebooks

1. **`00_Build_RAG_From_Scratch.ipynb`** ⭐ THE CAPSTONE
   - Step-by-step walkthrough of every component
   - Each step explained with the "why", not just the "how"
   - Progressive build: start simple, add complexity one piece at a time
   - Final `RAGSystem` class: clean, reusable, documented
   - Mini evaluation run at the end to verify quality
   - Checklist of what to add before going to production

## 🏗️ System Architecture

```
Input: Document collection + User query
          ↓
┌─────────────────────────────────────┐
│ INDEXING PIPELINE (offline)         │
│  1. Load documents                  │
│  2. Chunk (sentence-aware, overlap) │
│  3. Embed (sentence-transformers)   │
│  4. Store (in-memory or vector DB)  │
└─────────────────────────────────────┘
          ↓
┌─────────────────────────────────────┐
│ QUERY PIPELINE (online)             │
│  1. Embed query                     │
│  2. Retrieve top-K candidates       │
│  3. Rerank with CrossEncoder        │
│  4. Build prompt with context       │
│  5. Generate with LLM               │
│  6. Return answer + sources         │
└─────────────────────────────────────┘
          ↓
Output: Grounded answer with citations
```

## 🚀 Quick Start

```python
from rag_system import RAGSystem

# Build your system
rag = RAGSystem(
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",
    reranker_model="cross-encoder/ms-marco-MiniLM-L-6-v2",
    llm="claude-3-5-sonnet-20241022",
    chunk_size=512,
    chunk_overlap=50,
    top_k_retrieve=20,
    top_k_rerank=5
)

# Index your documents
rag.index(documents=["path/to/doc1.txt", "path/to/doc2.pdf"])

# Query
result = rag.query("How does BERT handle out-of-vocabulary words?")
print(result.answer)
print(result.sources)  # list of (text, score, metadata)
```

## 📋 What's Covered Step by Step

| Step | Notebook Section | Earlier Coverage |
|------|-----------------|-----------------|
| Chunking | §2: Smart chunking | `1_embeddings/06_Sentence_Tokenization` |
| Embedding | §3: Encode chunks | `1_embeddings/`, `2_retrieval/01` |
| Retrieval | §4: Hybrid search | `2_retrieval/03_Hybrid_Retrieval` |
| Reranking | §5: CrossEncoder | `2_retrieval/05_Reranking_Techniques` |
| Prompting | §6: RAG prompt | `4_generation/01_Prompt_Engineering` |
| Citations | §7: Parse + verify | `4_generation/03_Grounding_and_Citations` |
| Evaluation | §8: Mini benchmark | `6_evaluation/03_End_to_End_Evaluation` |

## 💡 Design Decisions Explained

**Why sentence-aware chunking over fixed-size?**
Fixed character windows break sentences mid-thought, which degrades embedding quality.

**Why rerank after retrieval?**
Embedding-based retrieval maximises recall. CrossEncoder reranking maximises precision. The two-stage approach gets both.

**Why 20 candidates → rerank to 5?**
Reranking is expensive (one forward pass per pair). Retrieve broadly, then rerank a manageable set.

**Why citations in the prompt?**
Forces the LLM to anchor claims to specific sources, making hallucination detection straightforward.

## 📖 Learning Path

**This is the final notebook in the series.** Complete these first for the best experience:
1. `0_foundations/` — understand the big picture
2. `2_retrieval/` — understand the retrieval stage
3. `4_generation/` — understand the generation stage
4. `6_evaluation/` — understand how to measure quality

**Coming here directly?**
The notebook is designed to be self-contained. Every design decision is explained inline.

## 🎓 Production Checklist

After completing the notebook, add these before going live:

- [ ] Move from in-memory storage to a proper vector database (Chroma, Pinecone, Weaviate)
- [ ] Add input validation and rate limiting (see `7_deployment/`)
- [ ] Implement query caching for repeated queries
- [ ] Add monitoring: latency per stage, cache hit rate, retrieval scores
- [ ] Run on your domain's benchmark (see `12_datasets_benchmarks/`)
- [ ] Get domain-expert review of answers before deploying in regulated industries (see `9_industry_verticals/`)

## 🔗 What Comes After This

You've now built, evaluated, and understand a complete RAG system. Where to go next:

- **Improve retrieval:** `3_search_techniques/`, `10_cutting_edge_research/00_RAPTOR`
- **Add agentic behaviour:** `5_advanced_rag/01_Agentic_RAG`
- **Deploy it:** `7_deployment/`
- **Use a framework:** `11_tools_frameworks/` — translate what you built into LangChain/LlamaIndex

## 🔧 Installation

```bash
pip install sentence-transformers rank-bm25 anthropic nltk scikit-learn
```

## 🤝 Contributing

Found an issue or want to add a workshop? Open an issue or PR!

---

**You made it.** You now understand every component of a production RAG system — from tokenization to deployment. Go build something! 🚀
