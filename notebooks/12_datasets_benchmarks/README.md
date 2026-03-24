# 📊 Datasets & Benchmarks - Measure Against the Standard

Knowing your RAG system works on your test documents is a start. Knowing it performs competitively on standard benchmarks is proof. This folder introduces the datasets the research community uses to evaluate RAG.

## 🎯 What You'll Learn

- Which standard datasets are used to evaluate RAG retrieval and generation
- How to load and use them in your evaluation pipeline
- Which benchmark to use for which type of RAG task
- How to compute and report standard metrics (Recall@K, MRR)

## 📚 Notebooks

1. **`00_RAG_Evaluation_Datasets.ipynb`** ⭐ THE ESSENTIAL GUIDE
   - Overview of the major benchmarks: MS MARCO, BEIR, HotpotQA, NaturalQuestions, TriviaQA
   - How to load each dataset (HuggingFace `datasets` library)
   - Which benchmark to use for which task
   - Mini evaluation: compute Recall@K and MRR on a subset
   - How to interpret benchmark scores vs SOTA results

## 📊 Benchmark Overview

| Dataset | Task | Size | Use When |
|---------|------|------|----------|
| **MS MARCO** | Passage retrieval | 8.8M passages | General retrieval baseline |
| **BEIR** | 18 retrieval tasks | Varies | Cross-domain generalisation |
| **HotpotQA** | Multi-hop QA | 113K questions | Complex reasoning chains |
| **NaturalQuestions** | Open-domain QA | 307K questions | Real user queries from Google |
| **TriviaQA** | Trivia QA | 95K questions | General knowledge retrieval |

## 🚀 Quick Start

```python
from datasets import load_dataset

# MS MARCO — passage retrieval
dataset = load_dataset("ms_marco", "v1.1", split="validation")
query = dataset[0]["query"]
passages = dataset[0]["passages"]["passage_text"]
answers = dataset[0]["answers"]

# NaturalQuestions
nq = load_dataset("natural_questions", split="validation")
question = nq[0]["question"]["text"]

# HotpotQA — multi-hop reasoning
hotpot = load_dataset("hotpot_qa", "fullwiki", split="validation")
question = hotpot[0]["question"]
supporting_facts = hotpot[0]["supporting_facts"]
```

## 💡 Choosing the Right Benchmark

```
Building a general-purpose RAG system?
  → Start with MS MARCO (most widely cited)

Testing generalisation to new domains?
  → Use BEIR (18 different retrieval tasks)

Your RAG needs to answer complex, multi-step questions?
  → HotpotQA (specifically designed for multi-hop)

Optimising for real user queries?
  → NaturalQuestions (from actual Google searches)

Quick sanity check on factual recall?
  → TriviaQA
```

## 📈 Interpreting Benchmark Scores

### What good looks like (retrieval, top-5)

| Metric | Poor | Acceptable | Good | Excellent |
|--------|------|------------|------|-----------|
| **Recall@5** | < 0.5 | 0.5-0.7 | 0.7-0.85 | > 0.85 |
| **MRR** | < 0.4 | 0.4-0.6 | 0.6-0.75 | > 0.75 |
| **NDCG@10** | < 0.4 | 0.4-0.55 | 0.55-0.70 | > 0.70 |

*These are rough guides — thresholds vary by dataset and task.*

## 📖 Learning Path

**Adding benchmarks to your evaluation workflow:**
1. `00_RAG_Evaluation_Datasets.ipynb`
2. Pick the benchmark closest to your use case
3. Run your RAG system on a subset (100-1000 examples)
4. Compare against published baselines

**Preparing for a paper or technical report:**
1. Run on BEIR for the broadest coverage
2. Report MRR, NDCG@10, and Recall@K for comparability

## 🎓 Production Checklist

- [ ] Choose the benchmark most similar to your production queries
- [ ] Use the same metric definitions as the benchmark's leaderboard
- [ ] Sample a manageable subset (1000 examples) before running the full benchmark
- [ ] Document your preprocessing steps so results are reproducible
- [ ] Compare against a simple BM25 baseline before celebrating your score

## 🔗 What's Next?

- **`6_evaluation/`** — build your own custom test set for your specific domain
- **`10_cutting_edge_research/02_LLM_as_Judge.ipynb`** — LLM-as-Judge for generation quality
- **`13_tutorials_workshops/`** — the capstone notebook includes a mini benchmark run

## 🔧 Installation

```bash
pip install datasets evaluate pytrec_eval
```

## 📝 Additional Resources

- [BEIR GitHub](https://github.com/beir-cellar/beir)
- [MS MARCO leaderboard](https://microsoft.github.io/msmarco/)
- [MTEB Leaderboard (embeddings)](https://huggingface.co/spaces/mteb/leaderboard)

## 🤝 Contributing

Want to add a notebook for a new benchmark? Open a PR!

---

**Remember:** A benchmark number without context is meaningless. Always compare against a simple baseline! 📊
