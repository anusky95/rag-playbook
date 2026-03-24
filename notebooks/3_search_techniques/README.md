# 🔎 Search Techniques - Make Retrieval Better

Basic retrieval often fails on complex or ambiguous questions. This folder teaches five techniques that dramatically improve what documents your RAG system finds.

## 🎯 Why Search Techniques Matter

```
User asks a vague question → Basic search misses the right docs → Bad answer ❌
User asks a vague question → Query expansion finds synonyms → Right docs → Good answer ✅
```

These techniques sit between the user's query and your retrieval system, reshaping the question before it hits the index.

## 📚 Notebooks (In Order)

### Foundation
1. **`00_Introduction_to_Search_Techniques.ipynb`** ⭐ START HERE
   - Overview of all 5 techniques and when to use each
   - Impact benchmarks: which technique improves recall the most?
   - Decision framework for picking the right approach
   - When basic search is good enough

### Core Techniques
2. **`01_Query_Expansion.ipynb`** 🔥
   - WordNet-based expansion (synonyms)
   - LLM-based expansion (rephrasings)
   - Embedding-based expansion (nearest neighbour terms)
   - Pseudo Relevance Feedback (PRF)
   - Production `QueryExpander` class

3. **`02_Multi_Query_Generation.ipynb`**
   - Generate multiple variations of the user's question using an LLM
   - Search with all variations, fuse results
   - Reciprocal Rank Fusion (RRF) to merge ranked lists
   - When multi-query helps (ambiguous questions, varied phrasing)

4. **`03_HyDE_Hypothetical_Documents.ipynb`** 🔥
   - Hypothetical Document Embeddings — generate a fake answer, embed it, search with that
   - Why searching with answers finds better matches than searching with questions
   - Implementation with any LLM
   - Performance comparison vs standard query embedding

5. **`04_Query_Decomposition.ipynb`**
   - Break complex, multi-part questions into sub-queries
   - Search each sub-query independently
   - Merge and deduplicate results
   - Useful for: "Compare X and Y" or "What did A do in year B?"

6. **`05_Routing_and_Filtering.ipynb`**
   - Metadata filtering: restrict search to relevant document subsets
   - Semantic routing: send the query to the right index
   - Date, category, and source filters
   - Production `QueryRouter` class

## 🚀 Quick Start

```python
# Query Expansion
from query_expander import QueryExpander

expander = QueryExpander(method='llm')
expanded_queries = expander.expand("What are transformer models?")
# Returns: ["What are transformer models?", "How do attention mechanisms work?", ...]

# HyDE
from hyde import HyDERetriever

retriever = HyDERetriever(llm=your_llm, embedder=your_embedder)
results = retriever.search("What causes inflation?")
# Generates a hypothetical answer first, then searches with it

# Multi-Query
from multi_query import MultiQueryRetriever

retriever = MultiQueryRetriever(llm=your_llm, base_retriever=your_retriever)
results = retriever.search("machine learning for beginners")
# Generates 3-5 query variants, fuses results with RRF
```

## 📊 Technique Comparison

| Technique | Best For | Complexity | Latency Added |
|-----------|----------|------------|---------------|
| **Query Expansion** | Broad vocabulary gaps | Low | +10ms |
| **Multi-Query** | Ambiguous questions | Medium | +100-300ms |
| **HyDE** | Questions phrased differently than documents | Medium | +200-500ms |
| **Decomposition** | Multi-part or comparison questions | High | +300-800ms |
| **Routing/Filtering** | Large, multi-domain indexes | Low | +5ms |

## 🎯 Decision Tree

```
Is the query ambiguous or phrased differently than your docs?
  └─ Yes → Try HyDE first

Does the query have multiple parts ("and", "compare", "versus")?
  └─ Yes → Query Decomposition

Do you have multiple indexes or document categories?
  └─ Yes → Routing + Filtering

Is recall too low on straightforward queries?
  └─ Yes → Query Expansion or Multi-Query
```

## 📖 Learning Path

**Beginner:**
1. `00_Introduction_to_Search_Techniques.ipynb`
2. `01_Query_Expansion.ipynb`

**Intermediate:**
1. `02_Multi_Query_Generation.ipynb`
2. `03_HyDE_Hypothetical_Documents.ipynb`

**Advanced:**
1. `04_Query_Decomposition.ipynb`
2. `05_Routing_and_Filtering.ipynb`
3. Combine multiple techniques in a pipeline

## 🎓 Production Checklist

- [ ] Profile where retrieval is failing before adding techniques
- [ ] Test each technique independently before combining
- [ ] Measure latency impact at your expected query volume
- [ ] Add query expansion as a fallback when retrieval scores are low
- [ ] Use filtering to reduce noise in large indexes

## 🔗 What's Next?

- **`4_generation/`** — now that you retrieve the right context, learn how to use it
- **`5_advanced_rag/`** — agentic RAG uses these techniques dynamically
- **`6_evaluation/`** — measure whether these techniques actually help on your data

## 🔧 Installation

```bash
pip install sentence-transformers rank-bm25 nltk openai anthropic
```

## 🤝 Contributing

Found an issue or want to add a notebook? Open an issue or PR!

---

**Remember:** The best retrieval technique depends on your data. Profile first, then optimise! 🔍
