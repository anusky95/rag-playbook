# 🌱 Foundations - Start Here

Welcome to the **ULTIMATE RAG** course! This folder is your entry point. Before writing a single line of retrieval code, you'll build a clear mental model of what RAG is and why it exists.

## 📚 What You'll Learn

- Why LLMs have a knowledge problem — and how RAG solves it
- The 3-step RAG loop: Retrieve → Augment → Generate
- How to build a working RAG system from scratch in under 50 lines

## 🗂️ Notebooks (In Order)

1. **`00_What_is_an_LLM.ipynb`** ⭐ START HERE
   - How LLMs work at a fundamental level
   - The next-word prediction intuition
   - Why LLMs hallucinate and can't access new information
   - The knowledge cutoff problem that RAG solves

2. **`01_What_is_RAG.ipynb`**
   - RAG explained with a simple analogy: "giving the LLM a textbook"
   - The 3-step RAG process with diagrams
   - When RAG helps (and when it doesn't)
   - Key vocabulary: chunk, embed, retrieve, augment, generate

3. **`02_Your_First_RAG.ipynb`** 🔥
   - Hands-on: a working RAG system end to end
   - Uses `sentence-transformers` and cosine similarity
   - Index your own documents and query them
   - Understand what each step does and why

## 🚀 Quick Start

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

# Index
documents = ["Paris is the capital of France.", "The Eiffel Tower is 330m tall."]
doc_embeddings = model.encode(documents)

# Retrieve
query = "What is the height of the Eiffel Tower?"
query_embedding = model.encode([query])
scores = cosine_similarity(query_embedding, doc_embeddings)[0]
best = documents[scores.argmax()]

# Generate (augment your prompt with `best`)
print(best)
```

## 💡 Key Concepts

| Term | Plain English |
|------|--------------|
| **Embedding** | A list of numbers that captures the meaning of text |
| **Chunk** | A small piece of a document (e.g., one paragraph) |
| **Retrieval** | Finding the chunks most relevant to the user's question |
| **Augmentation** | Adding those chunks to the LLM prompt |
| **Generation** | The LLM writing an answer grounded in the retrieved context |

## 📖 Learning Path

**No prior NLP experience:**
1. `00_What_is_an_LLM.ipynb` — build the mental model
2. `01_What_is_RAG.ipynb` — understand the architecture
3. `02_Your_First_RAG.ipynb` — get hands on

**Already know LLMs:**
- Skip to `02_Your_First_RAG.ipynb` and then move to `1_embeddings/`

## 🔗 What's Next?

After finishing these notebooks:
- **`1_embeddings/`** — deep dive into tokenization and embedding models
- **`2_retrieval/`** — build a production-quality retrieval system
- **`4_generation/`** — learn how to prompt LLMs effectively with context

## 🔧 Installation

```bash
pip install sentence-transformers scikit-learn
```

## 🤝 Contributing

Found an issue or want to add a notebook? Open an issue or PR!

---

**Remember:** RAG is simple in concept — find relevant text, add it to the prompt. Everything else is optimisation. Start here, then keep going! 🚀
