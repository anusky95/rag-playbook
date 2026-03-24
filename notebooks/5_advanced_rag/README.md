# 🤖 Advanced RAG - When Basic RAG Isn't Enough

Some questions can't be answered with a single retrieve-then-generate pass. This folder covers three patterns that give the LLM control over when and how to search.

## 🎯 When Basic RAG Breaks Down

```
Basic RAG: query → retrieve → generate (one pass)

Fails on:
- "What did Alice recommend, and what language is that tool written in?" (needs 2 hops)
- "Find all papers that contradict claim X" (needs iterative search)
- Questions where the LLM doesn't know what it doesn't know
```

## 📚 Notebooks (In Order)

### Foundation
1. **`00_Introduction_to_Advanced_RAG.ipynb`** ⭐ START HERE
   - Why basic RAG fails on complex questions
   - Overview of Agentic RAG, Self-RAG, and Multi-Hop RAG
   - Decision guide: which pattern to use and when
   - Cost/latency trade-offs of each approach

### Core Patterns
2. **`01_Agentic_RAG.ipynb`** 🔥
   - The LLM uses `tool_use` to trigger searches
   - Decides *what* to search for and *when* to stop
   - Multi-turn search loop with stopping conditions
   - Prevents infinite loops and runaway API costs
   - Production `AgenticRAG` class

3. **`02_Self_RAG.ipynb`** 🔥
   - The LLM critiques its own retrieval and generation
   - Three self-check questions: Do I need retrieval? Are these docs relevant? Is my answer grounded?
   - Token-efficient implementation (no extra LLM calls for simple queries)
   - Improves faithfulness without human review

4. **`03_Multi_Hop_RAG.ipynb`**
   - Chain searches together for questions requiring multiple reasoning steps
   - Example: "What language does the tool Alice recommended use?" → find Alice's recommendation → look up that tool's language
   - Automatic hop detection and query chaining
   - Result merging across hops

## 🚀 Quick Start

```python
# Agentic RAG — LLM decides when/what to search
from agentic_rag import AgenticRAG

agent = AgenticRAG(llm=claude, retriever=your_retriever, max_steps=5)
answer = agent.answer("What is the history of BERT and how did it influence GPT?")
# LLM searches multiple times, synthesises a complete answer

# Self-RAG — LLM checks its own work
from self_rag import SelfRAG

system = SelfRAG(llm=claude, retriever=your_retriever)
answer = system.answer("What causes inflation?")
# LLM: Do I need retrieval? → Yes
# Retrieves docs → Are these relevant? → Yes
# Generates answer → Is this grounded? → Yes → return answer

# Multi-Hop RAG — automatic reasoning chains
from multi_hop_rag import MultiHopRAG

system = MultiHopRAG(llm=claude, retriever=your_retriever, max_hops=3)
answer = system.answer("What programming language was used in the tool recommended by the author of the REALM paper?")
```

## 📊 Pattern Comparison

| Pattern | When to Use | Extra Latency | Extra Cost |
|---------|-------------|---------------|------------|
| **Agentic RAG** | Open-ended research questions | 2-5× | 2-5× |
| **Self-RAG** | When hallucination risk is high | 1.5-2× | 1.5-2× |
| **Multi-Hop RAG** | Questions needing ≥2 reasoning steps | 2-4× | 2-4× |
| Basic RAG | Simple factual lookup | 1× | 1× |

## 💡 Key Concepts

### The Tool-Use Pattern (Agentic RAG)
```python
tools = [{
    "name": "search_documents",
    "description": "Search the knowledge base for relevant information",
    "parameters": {"query": {"type": "string"}}
}]

# LLM calls this tool as many times as needed, then synthesises
response = llm.generate(prompt, tools=tools)
```

### Self-Check Prompts (Self-RAG)
1. **Retrieval gate**: "Does answering this question require external information?"
2. **Relevance check**: "Is this retrieved passage relevant to the question?"
3. **Faithfulness check**: "Is this answer fully supported by the passage?"

## 📖 Learning Path

**Intermediate:**
1. `00_Introduction_to_Advanced_RAG.ipynb`
2. `02_Self_RAG.ipynb` — lowest complexity, high value

**Advanced:**
1. `01_Agentic_RAG.ipynb`
2. `03_Multi_Hop_RAG.ipynb`
3. Combine patterns (e.g., Agentic + Self-RAG)

## 🎓 Production Checklist

- [ ] Set a maximum step/hop limit to prevent runaway loops
- [ ] Add per-query cost tracking
- [ ] Implement timeouts for each LLM call
- [ ] Cache intermediate search results within a session
- [ ] Log which pattern fired and how many steps it took
- [ ] Degrade gracefully to basic RAG if advanced pattern times out

## 🔗 What's Next?

- **`6_evaluation/`** — measure whether advanced patterns actually improve answers
- **`7_deployment/`** — deploy multi-step RAG as a production API
- **`10_cutting_edge_research/`** — RAPTOR, ColBERT, and other research-based improvements

## 🔧 Installation

```bash
pip install anthropic openai sentence-transformers
```

## 🤝 Contributing

Found an issue or want to add a notebook? Open an issue or PR!

---

**Remember:** Advanced patterns add latency and cost. Profile before adding them — sometimes better prompting or chunking is all you need! 🤖
