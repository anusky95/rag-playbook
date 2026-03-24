<div align="center">

# 🧠 RAG Playbook

### The only RAG resource you'll ever need — from first principles to production governance.

[![GitHub Stars](https://img.shields.io/github/stars/anusky95/ultimate-rag?style=social)](https://github.com/anusky95/ultimate-rag/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/anusky95/ultimate-rag?style=social)](https://github.com/anusky95/ultimate-rag/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python%203.10+-informational?logo=python)](requirements.txt)
[![Notebooks](https://img.shields.io/badge/Notebooks-50+-orange?logo=jupyter)](notebooks/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

<br/>

**50+ notebooks · Original TRUST Framework · From tokenization to enterprise governance**

[**TRUST Framework**](#-the-trust-framework) · [**All Notebooks**](#-everything-covered) · [**Quickstart**](#-quickstart) · [**Who It's For**](#-who-this-is-for)

</div>

---

## The Problem With Most RAG Resources

Most RAG tutorials show you a happy path: embed some docs, do a cosine search, call an LLM. Done.

Then you try to ship it.

Your retrieval misses half the relevant documents. Your LLM ignores the context and hallucinates. You have no idea if it's getting better or worse. There's no audit trail. Compliance says no.

**This repo was built for that moment** — the moment after the demo works but before it's actually usable.

> "Most RAG systems don't fail because of models — they fail because of everything _around_ them."
> — **Anupama Garani**

---

## ✨ The TRUST Framework

The centerpiece of this repo. An original 5-pillar framework for building RAG systems that don't fall apart in production.

![TRUST Framework Failure Zones](trust_framework/images/failure_stages.png)

Most RAG failures are predictable. They cluster around five zones — and each one has a name, an anti-pattern, and a concrete fix.

| Pillar | The Problem It Solves | The Fix |
|--------|-----------------------|---------|
| **T** — Targeted use cases | "We indexed everything and it answers nothing well" | Pick one high-pain question. Ship a 72-hour POC with 3 metrics. |
| **R** — Reliable metadata | Stale docs, missing owners, broken tables get indexed and cited | Block ingestion without `owner`, `doc_type`, `last_verified_date`. Table-aware chunking. |
| **U** — User-aligned prompting | Generic prompts that work for engineers but fail for end users | Co-create prompts with SMEs. Role-specific templates. Adversarial testing in CI. |
| **S** — Scalable evaluation | "It seems fine" — no golden set, no regression, no metrics | ≥50 Q/A pairs. Nightly CI scoring precision, recall, hallucination rate. |
| **T** — Trust through governance | PII leaks, no audit trail, can't answer "what did it say to user X?" | Pre/post PII redaction. Immutable logs. RBAC on sources and outputs. |

**→ Run it yourself:** [`trust_framework/RAG_Implementation.ipynb`](trust_framework/RAG_Implementation.ipynb)

**→ Full docs:** [`trust_framework/README.md`](trust_framework/README.md)

---

## 📚 Everything Covered

50+ notebooks across 14 sections. Every notebook builds on the previous one.

### Section 0 — Foundations
*Build intuition before writing code.*

| Notebook | What You Learn |
|----------|---------------|
| `00_What_is_an_LLM.ipynb` | How LLMs work, why they hallucinate, the knowledge cutoff problem |
| `01_What_is_RAG.ipynb` | The 3-step RAG loop (Retrieve → Augment → Generate), when RAG helps |
| `02_Your_First_RAG.ipynb` | A working RAG system in under 50 lines using `sentence-transformers` |

### Section 1 — Embeddings & Tokenization
*The foundation of every RAG pipeline.*

| Notebook | What You Learn |
|----------|---------------|
| `00_Tokenization_Overview.ipynb` | How text becomes numbers, impact on RAG |
| `01_Word_Tokenization.ipynb` | Word-level basics, vocabulary building, when not to use it |
| `02_Subword_Tokenization_BPE.ipynb` | BPE — used in GPT-2, GPT-3, GPT-4 |
| `03_WordPiece_Tokenization.ipynb` | WordPiece — used in BERT, E5, DistilBERT |
| `04_SentencePiece_Tokenization.ipynb` | Language-agnostic — used in T5, mT5, multilingual RAG |
| `05_Character_Tokenization.ipynb` | Character-level, why modern RAG avoids it |
| `06_Sentence_Tokenization.ipynb` | **Essential for RAG chunking** — sentence splitting with overlap |
| `07_Tokenization_Comparison_Guide.ipynb` | Side-by-side comparison, decision tree, production checklist |

### Section 2 — Retrieval
*The most critical stage. Bad retrieval = bad answers, no matter the LLM.*

| Notebook | What You Learn |
|----------|---------------|
| `00_Introduction_to_Retrieval.ipynb` | Sparse vs dense vs hybrid, key metrics |
| `01_Dense_Retrieval_Embeddings.ipynb` | Semantic search with BERT/E5/BGE, similarity metrics |
| `02_Sparse_Retrieval_BM25.ipynb` | BM25 — the industry-standard keyword search algorithm |
| `03_Hybrid_Retrieval.ipynb` | **Production standard** — RRF fusion of sparse + dense |
| `04_Vector_Databases.ipynb` | Pinecone, Weaviate, Chroma — when and how to use them |
| `05_Reranking_Techniques.ipynb` | CrossEncoder reranking, multi-stage retrieval pipelines |
| `06_Similarity_Metrics.ipynb` | Cosine, dot product, Euclidean — when each one matters |

### Section 3 — Search Techniques
*What to do when basic retrieval misses documents.*

| Notebook | What You Learn |
|----------|---------------|
| `00_Introduction_to_Search_Techniques.ipynb` | Overview of 5 techniques, when to use each, latency trade-offs |
| `01_Query_Expansion.ipynb` | WordNet, LLM-based, embedding-based expansion + Pseudo Relevance Feedback |
| `02_Multi_Query_Generation.ipynb` | Generate query variants, search all, fuse with RRF |
| `03_HyDE_Hypothetical_Documents.ipynb` | **Searching with answers, not questions** — why it works, how to implement |
| `04_Query_Decomposition.ipynb` | Break "Compare X and Y" into sub-queries, merge results |
| `05_Routing_and_Filtering.ipynb` | Metadata filtering, semantic routing, multi-index RAG |

### Section 4 — Generation
*Retrieved the right docs — now make the LLM actually use them.*

| Notebook | What You Learn |
|----------|---------------|
| `00_Introduction_to_Generation.ipynb` | What can go wrong after retrieval, failure mode taxonomy |
| `01_Prompt_Engineering_for_RAG.ipynb` | Naive → production prompt progression, system/user split, citation forcing |
| `02_Context_Window_Management.ipynb` | Token budgets, "lost in the middle" fix, context compression |
| `03_Grounding_and_Citations.ipynb` | Force `[Source N]` citations, parse and verify them, faithfulness checks |
| `04_Handling_Edge_Cases.ipynb` | No docs found, conflicting sources, out-of-scope queries, production checklist |

### Section 5 — Advanced RAG
*When a single retrieve-then-generate pass isn't enough.*

| Notebook | What You Learn |
|----------|---------------|
| `00_Introduction_to_Advanced_RAG.ipynb` | When basic RAG breaks, overview of 3 patterns, cost/latency trade-offs |
| `01_Agentic_RAG.ipynb` | LLM uses `tool_use` to search multiple times, stopping conditions |
| `02_Self_RAG.ipynb` | LLM checks: "Do I need retrieval? Are these relevant? Is my answer grounded?" |
| `03_Multi_Hop_RAG.ipynb` | Chain searches for multi-step questions, automatic hop detection |

### Section 6 — Evaluation
*You can't improve what you don't measure.*

| Notebook | What You Learn |
|----------|---------------|
| `00_Introduction_to_Evaluation.ipynb` | Why you need both retrieval AND generation metrics, TP/FP/FN in RAG |
| `01_Retrieval_Metrics.ipynb` | Precision@K, Recall@K, MRR, NDCG — implementation and interpretation |
| `02_Generation_Metrics.ipynb` | Exact Match, Token F1, Semantic Similarity, Faithfulness Score |
| `03_End_to_End_Evaluation.ipynb` | **Full harness** — test set → run RAG → diagnose whether retrieval or generation is the bottleneck |

### Section 7 — Deployment
*Getting RAG out of the notebook and into the world.*

| Notebook / File | What You Learn |
|----------|---------------|
| `00_Serving_RAG_with_FastAPI.ipynb` | REST API with Pydantic models, health check, async handlers |
| `01_Production_Checklist.ipynb` | Input validation, rate limiting, latency logging, query caching |
| `rag_api.py` | Ready-to-run FastAPI application |

### Section 8 — Case Studies
*Real patterns for real problems.*

| Notebook | What You Build |
|----------|---------------|
| `00_QA_Bot.ipynb` | Q&A chatbot over your own documents with citations |
| `01_Document_Search.ipynb` | Semantic search engine with keyword vs semantic comparison |
| `02_Code_Assistant.ipynb` | RAG over a codebase, chunked by function/class with line metadata |

### Section 9 — Industry Verticals
*RAG in regulated industries has different rules.*

| Notebook | What You Learn |
|----------|---------------|
| `00_RAG_for_Legal.ipynb` | Mandatory citations, jurisdiction awareness, what AI must never claim |
| `01_RAG_for_Medical.ipynb` | Evidence levels (RCT vs cohort vs expert), clinical disclaimers |
| `02_RAG_for_Finance.ipynb` | Exact number preservation, time-period citations, staleness filtering |

### Section 10 — Cutting Edge Research
*State-of-the-art techniques beyond standard RAG.*

| Notebook | What You Learn |
|----------|---------------|
| `00_RAPTOR.ipynb` | Hierarchical summarisation index — search at overview/summary/detail levels |
| `01_ColBERT_Late_Interaction.ipynb` | One vector per token, MaxSim scoring — better paraphrase matching |
| `02_LLM_as_Judge.ipynb` | Use an LLM to score faithfulness and relevance — foundation of RAGAS |

### Section 11 — Tools & Frameworks
*Use battle-tested libraries instead of building everything from scratch.*

| Notebook | What You Learn |
|----------|---------------|
| `00_LangChain_RAG.ipynb` | Full LangChain pipeline, LCEL chains, 100+ integrations |
| `01_LlamaIndex_RAG.ipynb` | LlamaIndex's RAG-first abstractions, RouterQueryEngine, SummaryIndex |

### Section 12 — Datasets & Benchmarks
*Measure against the standard, not just your own test documents.*

| Notebook | What You Learn |
|----------|---------------|
| `00_RAG_Evaluation_Datasets.ipynb` | MS MARCO, BEIR, HotpotQA, NaturalQuestions, TriviaQA — when to use each |

### Section 13 — Tutorials & Workshops (Capstone)
*Everything comes together.*

| Notebook | What You Build |
|----------|---------------|
| `00_Build_RAG_From_Scratch.ipynb` | **Full `RAGSystem` class** — chunk → embed → hybrid retrieve → rerank → prompt → generate → evaluate |

---

## 🚀 Quickstart

```bash
git clone https://github.com/anusky95/ultimate-rag.git
cd ultimate-rag
pip install -r requirements.txt
```

**Run the TRUST Framework (the original contribution):**
```bash
jupyter notebook trust_framework/RAG_Implementation.ipynb
```

**Start the learning path from zero:**
```bash
jupyter notebook notebooks/0_foundations/00_What_is_an_LLM.ipynb
```

**Jump straight to the capstone:**
```bash
jupyter notebook notebooks/13_tutorials_workshops/00_Build_RAG_From_Scratch.ipynb
```

---

## 🎯 Who This Is For

| If you are... | Go here first |
|---------------|--------------|
| New to RAG | [`0_foundations/`](notebooks/0_foundations/) |
| Know RAG, building for production | [`trust_framework/`](trust_framework/) |
| ML engineer needing evaluation tooling | [`6_evaluation/`](notebooks/6_evaluation/) |
| Building in legal / medical / finance | [`9_industry_verticals/`](notebooks/9_industry_verticals/) |
| Want the latest research (RAPTOR, ColBERT) | [`10_cutting_edge_research/`](notebooks/10_cutting_edge_research/) |
| Prefer LangChain / LlamaIndex | [`11_tools_frameworks/`](notebooks/11_tools_frameworks/) |
| Want to skip straight to the full build | [`13_tutorials_workshops/`](notebooks/13_tutorials_workshops/) |

---

## 🤝 Contributing

PRs welcome. When opening one, reference which **TRUST pillar** it strengthens.

Looking for: ingestion validators, chunking recipes, eval metrics, role-specific prompt templates, new industry verticals.

---

## Maintainer

**Anupama Garani** — AI & ML Systems · RAG & Evaluation · Governance

[![GitHub](https://img.shields.io/badge/GitHub-anusky95-181717?logo=github)](https://github.com/anusky95)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Anupama%20Garani-0077B5?logo=linkedin)](https://www.linkedin.com/in/anupamagarani)

---

## License

MIT — see [LICENSE](./LICENSE)

---

<div align="center">

**If this saved you from a bad RAG deployment, star it. ⭐**

_RAG isn't just a retrieval technique — it's an operating system for enterprise knowledge. Build it with **TRUST**._

</div>
