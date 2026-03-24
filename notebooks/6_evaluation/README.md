# 📏 Evaluation - Measure What Matters

You can't improve what you don't measure. This folder teaches you to systematically evaluate both the retrieval and generation stages of your RAG system.

## 🎯 Why Evaluation Matters

```
Without evaluation: "It seems to work well" (guessing)
With evaluation:    "Recall@5 = 0.72, Faithfulness = 0.89" (knowing)
```

Evaluation lets you catch regressions, compare retrieval strategies, and diagnose whether problems are in retrieval or generation.

## 📚 Notebooks (In Order)

### Foundation
1. **`00_Introduction_to_Evaluation.ipynb`** ⭐ START HERE
   - Why you need BOTH retrieval and generation metrics
   - Defining TP, FP, FN in the RAG context
   - Overview of the evaluation pipeline
   - Building a test set from scratch

### Core Metrics
2. **`01_Retrieval_Metrics.ipynb`** 🔥
   - Precision@K: of the K docs retrieved, what fraction are relevant?
   - Recall@K: of all relevant docs, what fraction did you retrieve?
   - Mean Reciprocal Rank (MRR): was the best doc near the top?
   - Normalised Discounted Cumulative Gain (NDCG): graded relevance ranking
   - Implementation and interpretation for each metric

3. **`02_Generation_Metrics.ipynb`** 🔥
   - Exact Match and Token F1 (lexical)
   - Semantic Similarity (embedding-based)
   - Faithfulness Score: does the answer stay within the context?
   - Worked examples on 3 test cases showing how each metric behaves differently
   - When to use which metric

4. **`03_End_to_End_Evaluation.ipynb`**
   - Complete evaluation harness: build test set → run RAG → measure both stages → diagnose bottlenecks
   - Identifying whether your bottleneck is retrieval or generation
   - Tracking metrics over time as you iterate
   - Production evaluation loop

## 🚀 Quick Start

```python
from rag_evaluator import RAGEvaluator

evaluator = RAGEvaluator(rag_system=your_rag)

# Build test set
test_cases = [
    {"query": "What is BERT?", "relevant_doc_ids": ["doc_42"], "expected_answer": "BERT is..."},
    # ...
]

# Run evaluation
results = evaluator.evaluate(test_cases, top_k=5)

print(f"Retrieval  → Recall@5: {results.recall_at_5:.2f}, MRR: {results.mrr:.2f}")
print(f"Generation → Faithfulness: {results.faithfulness:.2f}, Semantic Sim: {results.semantic_sim:.2f}")
```

## 📊 Metrics at a Glance

### Retrieval Metrics

| Metric | Measures | Good Value |
|--------|----------|------------|
| **Precision@K** | Relevance of retrieved docs | > 0.7 |
| **Recall@K** | Coverage of relevant docs | > 0.8 |
| **MRR** | Rank of first relevant doc | > 0.7 |
| **NDCG@K** | Quality of ranked order | > 0.75 |

### Generation Metrics

| Metric | Measures | Good Value |
|--------|----------|------------|
| **Exact Match** | Perfect string match | Depends on task |
| **Token F1** | Lexical overlap | > 0.6 |
| **Semantic Sim** | Meaning similarity | > 0.8 |
| **Faithfulness** | Grounded in context | > 0.9 |

## 💡 Diagnosing Bottlenecks

```
Low Recall@5 + Low Answer Quality → Fix retrieval first
High Recall@5 + Low Faithfulness  → Fix generation (prompting)
High Recall@5 + Low Semantic Sim  → Improve answer quality / context usage
Low MRR + OK Recall@5             → Add reranking
```

## 📖 Learning Path

**Beginner:**
1. `00_Introduction_to_Evaluation.ipynb`
2. `01_Retrieval_Metrics.ipynb`

**Intermediate:**
1. `02_Generation_Metrics.ipynb`
2. Build your own test set on your domain

**Advanced:**
1. `03_End_to_End_Evaluation.ipynb`
2. Automate evaluation in CI/CD
3. See `12_datasets_benchmarks/` for standard benchmarks

## 🎓 Production Checklist

- [ ] Create a golden test set of ≥100 query/answer pairs
- [ ] Run evaluation after every significant change
- [ ] Track Recall@K and Faithfulness as your primary metrics
- [ ] Set minimum thresholds before deploying (e.g., Faithfulness > 0.90)
- [ ] Log evaluation results to a dashboard
- [ ] Re-evaluate when document corpus changes significantly

## 🔗 What's Next?

- **`7_deployment/`** — add evaluation logging to your production API
- **`10_cutting_edge_research/`** — LLM-as-Judge (notebook 02) for scalable evaluation
- **`12_datasets_benchmarks/`** — benchmark against MS MARCO, BEIR, and HotpotQA

## 🔧 Installation

```bash
pip install sentence-transformers scikit-learn numpy pandas
```

## 🤝 Contributing

Found an issue or want to add a notebook? Open an issue or PR!

---

**Remember:** Evaluation is not a one-time step — run it on every change. You can't steer without a compass! 📏
