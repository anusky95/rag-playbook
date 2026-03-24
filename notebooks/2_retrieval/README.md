# 🔍 Retrieval - The Heart of RAG

Welcome to the **RETRIEVAL** section - the most critical component of any RAG system! This folder contains everything you need to master information retrieval for production RAG.

## 🎯 Why Retrieval Matters

**Retrieval quality directly determines RAG quality:**
```
Bad Retrieval → Wrong Context → Bad Answers ❌
Good Retrieval → Right Context → Great Answers ✅
```

The best LLM in the world can't help if you feed it irrelevant context!

## 📚 Notebooks Overview

### Foundation
1. **`00_Introduction_to_Retrieval.ipynb`** ⭐ **START HERE**
   - What is retrieval and why it matters
   - Sparse vs Dense vs Hybrid
   - Key concepts and metrics
   - Simple implementations

### Core Methods
2. **`01_Dense_Retrieval_Embeddings.ipynb`** 🧠
   - Semantic search with embeddings
   - Popular models (BERT, E5, BGE)
   - Similarity metrics
   - Production-ready code

3. **`02_Sparse_Retrieval_BM25.ipynb`** 📊
   - BM25 algorithm (industry standard)
   - TF-IDF for comparison
   - Parameter tuning (k1, b)
   - Advanced preprocessing

4. **`03_Hybrid_Retrieval_Best_of_Both.ipynb`** 🚀 **PRODUCTION STANDARD**
   - Combining sparse + dense
   - Reciprocal Rank Fusion (RRF)
   - Linear combination
   - Real-world examples

### Advanced Topics
5. **`04_Vector_Databases.ipynb`** (Coming soon!)
   - Pinecone, Weaviate, Chroma
   - Index optimization
   - Scaling to millions of docs

6. **`05_Reranking_Techniques.ipynb`** (Coming soon!)
   - Cross-encoders
   - Multi-stage retrieval
   - Production optimization

## 🚀 Quick Start

### Basic Dense Retrieval
```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Encode
doc_embeddings = model.encode(documents)
query_embedding = model.encode(query)

# Search
scores = cosine_similarity([query_embedding], doc_embeddings)[0]
top_docs = documents[scores.argsort()[::-1][:5]]
```

### Basic Sparse Retrieval (BM25)
```python
from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize

# Index
tokenized_docs = [word_tokenize(doc.lower()) for doc in documents]
bm25 = BM25Okapi(tokenized_docs)

# Search
tokenized_query = word_tokenize(query.lower())
scores = bm25.get_scores(tokenized_query)
top_docs = documents[scores.argsort()[::-1][:5]]
```

### Production Hybrid Retrieval
```python
from hybrid_retriever import ProductionHybridRetriever

# Initialize
retriever = ProductionHybridRetriever(
    fusion_method='rrf',  # Reciprocal Rank Fusion
    k=60  # RRF constant
)

# Index
retriever.index(documents, metadata=metadata)

# Search
results = retriever.search(query, top_k=5)

# Save
retriever.save('index/')
```

## 📊 Method Comparison

| Method | Speed | Quality | Use Case | Implementation |
|--------|-------|---------|----------|----------------|
| **Dense** | ⚡⚡ | ⭐⭐⭐⭐ | Semantic search | Notebook 01 |
| **Sparse (BM25)** | ⚡⚡⚡ | ⭐⭐⭐ | Exact matching | Notebook 02 |
| **Hybrid** | ⚡⚡ | ⭐⭐⭐⭐⭐ | Production RAG | Notebook 03 |

### When to Use What?

**Dense Retrieval:**
- ✅ Semantic understanding needed
- ✅ Handling synonyms/paraphrases
- ✅ Multilingual search
- ✅ Conceptual queries

**Sparse Retrieval (BM25):**
- ✅ Exact keyword matching
- ✅ Technical docs (APIs, code)
- ✅ Product names/codes
- ✅ Legal/medical terminology

**Hybrid Retrieval:** 🏆
- ✅ **Production RAG systems** (RECOMMENDED)
- ✅ E-commerce search
- ✅ Enterprise search
- ✅ Any serious application

## 🔑 Key Concepts

### 1. Embeddings
```python
Text: "machine learning" 
   ↓
Vector: [0.23, -0.45, 0.12, ...] (768 dims)
   ↓
Similar texts have similar vectors!
```

### 2. Similarity Metrics
- **Cosine Similarity**: Angle between vectors (most common)
- **Dot Product**: Fast if normalized
- **Euclidean**: Geometric distance

### 3. BM25 Scoring
```
BM25 = IDF × (TF × (k1 + 1)) / (TF + k1 × (1 - b + b × doc_len/avg_len))

Parameters:
- k1: Term saturation (default 1.5)
- b: Length normalization (default 0.75)
```

### 4. Fusion Methods
- **RRF (Reciprocal Rank Fusion)**: `score = Σ 1/(k + rank)`
- **Linear**: `score = α×sparse + (1-α)×dense`
- **Convex**: Normalized linear combination

## 🎯 Decision Tree

```
Start
  ↓
Do you need exact keyword matching?
  ├─ Yes → Do you also need semantic understanding?
  │         ├─ Yes → Use Hybrid ✅
  │         └─ No → Use BM25
  │
  └─ No → Is it semantic/conceptual search?
            ├─ Yes → Use Dense
            └─ No → Use Hybrid (safest)

Default: Hybrid is almost always the best choice! 🚀
```

## 📈 Performance Benchmarks

### Speed (1M documents)
```
BM25:     10-50ms per query
Dense:    100-500ms per query  
Hybrid:   110-550ms per query
```

### Quality (Typical improvements)
```
BM25 alone:     70% relevance
Dense alone:    75% relevance
Hybrid:         85% relevance ⭐
```

## 💡 Best Practices

### For All Methods:
1. **Clean your data** - Remove duplicates, normalize text
2. **Chunk appropriately** - 256-512 tokens optimal
3. **Add metadata** - Source, date, category for filtering
4. **Monitor performance** - Track latency and relevance
5. **A/B test** - Compare methods on your data

### For Dense Retrieval:
1. **Choose right model** - Match to your domain
2. **Use batching** - 32-64 batch size for speed
3. **Normalize embeddings** - Use dot product instead of cosine
4. **Cache embeddings** - Save to disk, avoid recomputing
5. **GPU acceleration** - 10x faster on GPU

### For BM25:
1. **Tune parameters** - k1 and b for your corpus
2. **Preprocess text** - Stopwords, stemming, lowercasing
3. **Save tokenized docs** - Avoid re-tokenization
4. **Use efficient implementation** - rank-bm25 is fast

### For Hybrid:
1. **Start with RRF** - k=60 works great out of box
2. **Monitor fusion** - Track sparse vs dense contribution
3. **Save indexes** - Both BM25 and embeddings
4. **Test fusion methods** - RRF vs linear on your data

## 🔧 Installation

```bash
# Core dependencies
pip install sentence-transformers rank-bm25 scikit-learn nltk numpy

# Optional but recommended
pip install faiss-cpu  # or faiss-gpu for GPU
pip install transformers
pip install torch

# For production
pip install pinecone-client weaviate-client chromadb
```

## 📖 Learning Path

### Beginner (2-3 hours)
1. Start with `00_Introduction_to_Retrieval.ipynb`
2. Learn dense retrieval: `01_Dense_Retrieval_Embeddings.ipynb`
3. Understand sparse retrieval: `02_Sparse_Retrieval_BM25.ipynb`

### Intermediate (3-4 hours)
1. Master hybrid: `03_Hybrid_Retrieval_Best_of_Both.ipynb`
2. Compare all methods on your own data
3. Implement a simple RAG pipeline

### Advanced (4+ hours)
1. Explore vector databases: `04_Vector_Databases.ipynb`
2. Learn reranking: `05_Reranking_Techniques.ipynb`
3. Build production-ready system

## 🎓 Production Checklist

Before deploying your retrieval system:

- [ ] Choose retrieval method (hybrid recommended)
- [ ] Select appropriate embedding model
- [ ] Tune BM25 parameters (if using)
- [ ] Optimize chunk size (256-512 tokens)
- [ ] Add metadata support
- [ ] Implement score thresholds
- [ ] Cache embeddings/indexes
- [ ] Add monitoring and logging
- [ ] Load test at expected scale
- [ ] A/B test against baseline

## 🌟 Common Patterns

### Pattern 1: Basic RAG Retrieval
```python
# Simple hybrid retrieval
retriever = HybridRetriever(fusion_method='rrf')
retriever.index(documents)
results = retriever.search(query, top_k=5)
context = '\n'.join([r['document'] for r in results])
```

### Pattern 2: Filtered Retrieval
```python
# Retrieve with metadata filtering
results = retriever.search(
    query, 
    top_k=10,
    filters={'category': 'technical', 'date': '2024'}
)
```

### Pattern 3: Multi-Stage Retrieval
```python
# Stage 1: Hybrid retrieval (recall)
candidates = hybrid.search(query, top_k=100)

# Stage 2: Rerank (precision)
final = reranker.rerank(query, candidates, top_k=5)
```

### Pattern 4: Production Pipeline
```python
class RAGRetriever:
    def __init__(self):
        self.retriever = ProductionHybridRetriever()
        
    def retrieve(self, query, top_k=5):
        # Get results
        results = self.retriever.search(query, top_k=top_k)
        
        # Log for monitoring
        self.log_results(query, results)
        
        # Format for LLM
        context = self.format_context(results)
        
        return context
```

## 🔗 What's Next?

After mastering retrieval:
- **`3_search_techniques/`** - Advanced search algorithms
- **`4_generation/`** - LLM integration for RAG
- **`5_advanced_rag/`** - Multi-hop, agents, etc.
- **`6_evaluation/`** - Measure retrieval quality

## 📝 Additional Resources

### Papers
- [Dense Passage Retrieval (DPR)](https://arxiv.org/abs/2004.04906)
- [REALM: Retrieval-Augmented Language Models](https://arxiv.org/abs/2002.08909)
- [ColBERT: Efficient Passage Retrieval](https://arxiv.org/abs/2004.12832)

### Tools
- [Sentence Transformers](https://www.sbert.net/)
- [Rank-BM25](https://github.com/dorianbrown/rank_bm25)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Haystack](https://haystack.deepset.ai/)

### Benchmarks
- [BEIR Benchmark](https://github.com/beir-cellar/beir)
- [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)

## 🤝 Contributing

Found an issue or want to add a notebook? Open an issue or PR!

---

**Remember:** Retrieval is 80% of RAG quality! Master it, and your RAG system will shine! ✨

Ready? Start with `00_Introduction_to_Retrieval.ipynb`!