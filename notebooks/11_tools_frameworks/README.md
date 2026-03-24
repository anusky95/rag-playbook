# 🛠️ Tools & Frameworks - Don't Reinvent the Wheel

Building RAG from scratch is great for learning. For production, use battle-tested frameworks. This folder shows how LangChain and LlamaIndex implement the same RAG patterns you've already learned.

## 🎯 What You'll Learn

- How LangChain's abstractions map to the RAG pipeline you built in earlier notebooks
- How LlamaIndex differs from LangChain and when to prefer it
- When to use a framework vs rolling your own

## 📚 Notebooks

1. **`00_LangChain_RAG.ipynb`** 🦜
   - The LangChain RAG pipeline: `DocumentLoader → TextSplitter → Embeddings → VectorStore → Retriever → LLM → Chain`
   - How each LangChain abstraction maps to concepts from `2_retrieval/` and `4_generation/`
   - LCEL (LangChain Expression Language) for composing chains
   - Built-in integrations: Chroma, Pinecone, OpenAI, Anthropic
   - When LangChain excels: complex chains, multi-step agents, many integrations needed

2. **`01_LlamaIndex_RAG.ipynb`** 🦙
   - LlamaIndex's RAG primitives: `SimpleDirectoryReader → VectorStoreIndex → QueryEngine`
   - More RAG-focused than LangChain — less boilerplate for common patterns
   - Power features: `SummaryIndex`, `RouterQueryEngine`, `SubQuestionQueryEngine`
   - How `RouterQueryEngine` relates to `3_search_techniques/05_Routing_and_Filtering.ipynb`
   - When LlamaIndex excels: complex document hierarchies, multi-index routing

## 🚀 Quick Start

```python
# LangChain RAG in ~20 lines
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatAnthropic

loader = DirectoryLoader("./docs/")
docs = loader.load()
chunks = RecursiveCharacterTextSplitter(chunk_size=500).split_documents(docs)
db = Chroma.from_documents(chunks, HuggingFaceEmbeddings())
qa = RetrievalQA.from_chain_type(llm=ChatAnthropic(), retriever=db.as_retriever())
answer = qa.run("What is RAG?")
```

```python
# LlamaIndex RAG in ~10 lines
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

documents = SimpleDirectoryReader("./docs/").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What is RAG?")
print(response)
```

## 📊 Framework Comparison

| Feature | LangChain | LlamaIndex |
|---------|-----------|------------|
| **Learning curve** | Steeper | Gentler for RAG |
| **RAG focus** | General purpose | RAG-first |
| **Integrations** | Very broad (100+ tools) | Narrower but deep |
| **Agents** | Excellent | Good |
| **Multi-index routing** | Manual | Built-in |
| **Best for** | Complex agentic pipelines | Document Q&A, multi-index |

## 💡 Framework vs From-Scratch

**Use a framework when:**
- You need integrations (Pinecone, Weaviate, many LLM providers)
- You want community-maintained connectors
- You're prototyping quickly
- Your team already uses the framework

**Roll your own when:**
- You need fine-grained control over retrieval logic
- You've outgrown framework abstractions
- Debugging the framework is costing more time than it saves
- Performance is critical and framework overhead matters

## 📖 Learning Path

**Recommended order:**
1. Complete `2_retrieval/` and `4_generation/` first — you'll understand what the framework is doing
2. `00_LangChain_RAG.ipynb` — more widely used in industry
3. `01_LlamaIndex_RAG.ipynb` — better for pure RAG use cases

**Already know one framework:**
- Read the other notebook to understand the trade-offs

## 🎓 Production Checklist

- [ ] Pin framework versions — both LangChain and LlamaIndex have frequent breaking changes
- [ ] Test integrations (vector stores, LLM providers) independently
- [ ] Monitor framework-added latency vs your from-scratch baseline
- [ ] Check framework's default chunking — it may not suit your documents
- [ ] Read the framework's changelog before upgrading

## 🔗 What's Next?

- **`5_advanced_rag/`** — both frameworks have agentic RAG support
- **`13_tutorials_workshops/`** — the capstone builds from scratch (useful contrast)
- **`7_deployment/`** — deploy framework-based RAG with FastAPI

## 🔧 Installation

```bash
# LangChain
pip install langchain langchain-community langchain-anthropic chromadb

# LlamaIndex
pip install llama-index llama-index-llms-anthropic llama-index-embeddings-huggingface
```

## 📝 Additional Resources

- [LangChain Documentation](https://python.langchain.com/docs/)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [LangChain vs LlamaIndex comparison](https://www.sbert.net/)

## 🤝 Contributing

Want to add a notebook for another framework (Haystack, DSPy)? Open a PR!

---

**Remember:** Frameworks are accelerators, not crutches. Understand the underlying patterns first! 🛠️
