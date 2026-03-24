# ✍️ Generation - Turning Retrieved Context into Answers

You've retrieved the right documents. Now what? This folder teaches you how to craft prompts that turn retrieved context into grounded, cited, trustworthy answers.

## 🎯 Why Generation Matters

```
Great retrieval + bad prompt → Hallucinated answer ❌
Great retrieval + great prompt → Grounded, cited answer ✅
```

The LLM doesn't automatically use context well — you have to design the prompt to make it.

## 📚 Notebooks (In Order)

### Foundation
1. **`00_Introduction_to_Generation.ipynb`** ⭐ START HERE
   - The generation step of the RAG pipeline
   - What can go wrong: bad prompts, context overflow, no docs found
   - Anatomy of a RAG prompt
   - Common failure modes and how to prevent them

### Core Skills
2. **`01_Prompt_Engineering_for_RAG.ipynb`** 🔥
   - Progression from naive to production-quality prompts
   - System message vs user message structure
   - Telling the LLM to answer *only* from context
   - Requiring citations in the output
   - Handling when the answer isn't in the context

3. **`02_Context_Window_Management.ipynb`** 🔥
   - Token budgets: how much context can you fit?
   - Greedy selection vs scored selection
   - The "lost in the middle" problem — put the best docs first and last
   - Truncation strategies that preserve meaning
   - Context compression with LLMs

4. **`03_Grounding_and_Citations.ipynb`**
   - Forcing the LLM to cite sources with `[Source N]` notation
   - Parsing citation patterns from LLM output
   - Faithfulness checks: does the answer actually follow from the context?
   - Detecting when the LLM ignores the context and hallucinates

5. **`04_Handling_Edge_Cases.ipynb`**
   - No relevant documents found → graceful fallback
   - Low-confidence retrieval → express uncertainty
   - Conflicting information across documents → surface the conflict
   - Out-of-scope queries → redirect appropriately
   - Production checklist for edge cases

## 🚀 Quick Start

```python
def build_rag_prompt(query: str, retrieved_docs: list[str]) -> str:
    context = "\n\n".join(
        f"[Source {i+1}]: {doc}" for i, doc in enumerate(retrieved_docs)
    )
    return f"""You are a helpful assistant. Answer the question using ONLY the sources below.
If the answer is not in the sources, say "I don't have enough information to answer this."
Always cite your sources using [Source N] notation.

Sources:
{context}

Question: {query}

Answer:"""

# Usage
docs = retriever.search(user_query, top_k=5)
prompt = build_rag_prompt(user_query, docs)
answer = llm.generate(prompt)
```

## 📊 Prompt Engineering Progression

| Level | Approach | Risk |
|-------|----------|------|
| Naive | "Answer this: {query}\n{context}" | High hallucination |
| Basic | Separate context section, no instructions | Medium hallucination |
| Intermediate | "Answer only from context" instruction | Low hallucination |
| **Production** | **System/user split + citations + fallback** | **Minimal hallucination** |

## 💡 Key Concepts

### The "Lost in the Middle" Problem
LLMs recall information better from the start and end of the context window. Put your most relevant chunks first and last:
```python
# Sort by relevance, then interleave best/worst
top_docs = sorted(docs, key=lambda x: x.score, reverse=True)
reordered = top_docs[::2] + top_docs[1::2][::-1]  # odd indices at start, even at end
```

### Context Budget Planning
```
Model context window:    128,000 tokens
System prompt:           ~500 tokens
User question:           ~50 tokens
Retrieved context:       up to ~6,000 tokens (12 × 500-token chunks)
LLM response:            up to ~1,000 tokens
Buffer:                  ~500 tokens
```

## 📖 Learning Path

**Beginner:**
1. `00_Introduction_to_Generation.ipynb`
2. `01_Prompt_Engineering_for_RAG.ipynb`

**Intermediate:**
1. `02_Context_Window_Management.ipynb`
2. `03_Grounding_and_Citations.ipynb`

**Advanced:**
1. `04_Handling_Edge_Cases.ipynb`
2. Combine with `5_advanced_rag/` for multi-turn grounded conversations

## 🎓 Production Checklist

- [ ] System message instructs the LLM to answer only from context
- [ ] Prompt includes a fallback for when the answer isn't in the context
- [ ] LLM is required to cite sources
- [ ] Citation parsing is implemented and tested
- [ ] Token counting prevents context overflow
- [ ] Edge cases (no docs, conflicting docs) are handled gracefully
- [ ] Faithfulness check runs on high-stakes queries

## 🔗 What's Next?

- **`5_advanced_rag/`** — agentic and self-checking RAG for complex queries
- **`6_evaluation/`** — measure faithfulness, citation accuracy, and answer quality
- **`8_case_studies/`** — see these prompting patterns applied to real use cases

## 🔧 Installation

```bash
pip install anthropic openai tiktoken
```

## 🤝 Contributing

Found an issue or want to add a notebook? Open an issue or PR!

---

**Remember:** A RAG system is only as trustworthy as its prompt. Design for grounding first! ✍️
