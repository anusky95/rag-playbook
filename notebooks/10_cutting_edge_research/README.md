# 🔬 Cutting Edge Research - Beyond Basic RAG

The RAG field moves fast. This folder covers three techniques from recent research that go well beyond standard retrieve-then-generate: hierarchical indexing, token-level retrieval, and LLM-based evaluation.

## 🎯 What You'll Learn

- How to build and query a tree of summaries for better long-document retrieval (RAPTOR)
- Why one vector per token outperforms one vector per document (ColBERT)
- How to use an LLM as an automatic evaluator — the foundation of RAGAS (LLM-as-Judge)

## 📚 Notebooks

1. **`00_RAPTOR.ipynb`** 🌳
   - **R**ecursive **A**bstractive **P**rocessing for **T**ree-**O**rganized **R**etrieval
   - Build a hierarchy: raw chunks → paragraph summaries → section summaries → document summary
   - Query at multiple levels: overview questions hit the top, detail questions hit the bottom
   - Excellent for long documents where chunk-level retrieval loses the big picture
   - Implementation: clustering + summarisation loop

2. **`01_ColBERT_Late_Interaction.ipynb`** 🎯
   - Standard RAG: one vector per document → coarse semantic matching
   - ColBERT: one vector **per token** → fine-grained matching
   - **MaxSim** scoring: for each query token, find its best matching document token
   - Better at paraphrase matching and out-of-vocabulary terms
   - Trade-off: higher storage cost, but faster at query time than cross-encoders

3. **`02_LLM_as_Judge.ipynb`** ⚖️
   - Use an LLM (e.g., Claude) to automatically rate retrieval relevance and answer faithfulness
   - Scale evaluation without human annotators
   - Foundation of the RAGAS framework
   - Calibration: how well does LLM-judge correlate with human judgment?
   - Prompt templates for faithfulness, relevance, and answer correctness

## 📊 Technique Comparison

| Technique | What It Improves | Overhead | Best For |
|-----------|-----------------|----------|----------|
| **RAPTOR** | Long-document understanding | 2-4× index time | Documents > 10 pages |
| **ColBERT** | Paraphrase & term matching | 50-100× storage | High-precision retrieval |
| **LLM-as-Judge** | Scalable evaluation | 1 LLM call per sample | Automated quality monitoring |

## 💡 Key Concepts

### RAPTOR: Hierarchical Indexing
```
Document
  ├─ Chunk 1 ─┐
  ├─ Chunk 2 ─┤─ Cluster A Summary ─┐
  ├─ Chunk 3 ─┘                     ├─ Section Summary ─┐
  ├─ Chunk 4 ─┐                     │                   ├─ Document Summary
  └─ Chunk 5 ─┴─ Cluster B Summary ─┘

Query → search all levels → pick best match level → retrieve
```

### ColBERT: MaxSim Scoring
```python
# Per-token embeddings
query_tokens   = encode_tokens("What is BERT?")   # shape: [Q, 128]
doc_tokens     = encode_tokens("BERT is a model") # shape: [D, 128]

# MaxSim: each query token finds its best match in the document
score = sum(max(cosine(q, d) for d in doc_tokens) for q in query_tokens)
```

### LLM-as-Judge: Faithfulness Prompt
```python
faithfulness_prompt = """
Given a context and an answer, rate how faithfully the answer is supported by the context.
Score: 1 (not supported) to 5 (fully supported, every claim traceable to the context).

Context: {context}
Answer: {answer}

Score:"""
```

## 📖 Learning Path

**Research-oriented:**
1. Read the RAPTOR and ColBERT papers linked in each notebook
2. `00_RAPTOR.ipynb` — build the tree index, see where it beats flat retrieval
3. `01_ColBERT_Late_Interaction.ipynb` — compare MaxSim vs cosine on your data

**Evaluation-focused:**
1. `02_LLM_as_Judge.ipynb`
2. Integrate with your evaluation harness from `6_evaluation/`

## 🎓 Production Checklist

- [ ] RAPTOR: set cluster size and number of levels based on document length
- [ ] RAPTOR: cache the tree index — rebuilding is expensive
- [ ] ColBERT: plan for token-level storage (10-50× more than document-level)
- [ ] LLM-as-Judge: calibrate against human ratings before trusting scores
- [ ] LLM-as-Judge: log judge scores alongside application metrics

## 🔗 What's Next?

- **`6_evaluation/`** — combine LLM-as-Judge with traditional retrieval metrics
- **`11_tools_frameworks/`** — LangChain and LlamaIndex have RAPTOR and ColBERT integrations
- **`13_tutorials_workshops/`** — the capstone notebook puts all techniques together

## 🔧 Installation

```bash
pip install sentence-transformers colbert-ai anthropic scikit-learn
```

## 📝 Papers

- [RAPTOR (Sarthi et al., 2024)](https://arxiv.org/abs/2401.18059)
- [ColBERT (Khattab & Zaharia, 2020)](https://arxiv.org/abs/2004.12832)
- [RAGAS (Es et al., 2023)](https://arxiv.org/abs/2309.15217)

## 🤝 Contributing

Want to add a new research technique? Open a PR!

---

**Remember:** Research techniques often have rough edges. Test on your data before committing to production! 🔬
