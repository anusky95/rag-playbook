# 🚀 Deployment - From Notebook to Production

Great RAG in a notebook is not the same as great RAG in production. This folder covers how to serve your RAG system as a REST API and harden it for real traffic.

## 🎯 What You'll Learn

- Wrapping a RAG system in a FastAPI application
- Designing clean request/response contracts
- Input validation, rate limiting, and caching
- Latency logging and graceful degradation

## 🗂️ Contents

### Notebooks
1. **`00_Serving_RAG_with_FastAPI.ipynb`** ⭐ START HERE
   - Convert your RAG system into REST API endpoints
   - Request and response models with Pydantic
   - Health check endpoint
   - Async handlers for concurrent requests
   - Running locally and testing with `curl`

2. **`01_Production_Checklist.ipynb`** 🔥
   - Input validation: length limits, injection prevention
   - Fallback answers when retrieval fails
   - Latency logging per stage (retrieval vs generation)
   - Query result caching with TTL
   - Rate limiting per API key
   - Graceful error responses

### Code
- **`rag_api.py`** — complete, runnable FastAPI application ready to deploy

## 🚀 Quick Start

```bash
# Run the API locally
pip install fastapi uvicorn pydantic
uvicorn rag_api:app --reload --port 8000

# Test it
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is RAG?", "top_k": 5}'
```

```python
# rag_api.py — core structure
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]
    latency_ms: float

@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    docs = retriever.search(request.query, top_k=request.top_k)
    answer = generator.generate(request.query, docs)
    return QueryResponse(answer=answer, sources=docs, latency_ms=...)

@app.get("/health")
async def health():
    return {"status": "ok"}
```

## 📊 Production Architecture

```
Client
  ↓
Rate Limiter
  ↓
Input Validator
  ↓
Cache Check ──hit──→ Return cached response
  ↓ miss
Retrieval (log latency)
  ↓
Generation (log latency)
  ↓
Response + Cache store
```

## 💡 Key Production Concerns

### Latency Budget
```
Target: < 2s end-to-end
  Retrieval:  100-500ms
  Generation: 500-1500ms
  Overhead:   < 100ms
```

### Input Validation
```python
class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000)
    top_k: int = Field(default=5, ge=1, le=20)
```

### Caching Strategy
- Cache by query hash (exact match)
- TTL: 1 hour for factual queries, shorter for time-sensitive domains
- Invalidate on corpus update

## 🎓 Production Checklist

- [ ] Input length limits enforced
- [ ] Rate limiting per API key / IP
- [ ] Health check endpoint responds < 100ms
- [ ] All errors return structured JSON (not stack traces)
- [ ] Latency logged per stage (retrieval, generation, total)
- [ ] Query cache implemented with TTL
- [ ] Fallback answer for retrieval failures
- [ ] Load tested at 2× expected peak traffic
- [ ] Secrets (API keys) in environment variables, not code
- [ ] Logging to structured log sink (e.g., CloudWatch, Datadog)

## 📖 Learning Path

**Intermediate:**
1. `00_Serving_RAG_with_FastAPI.ipynb`
2. Adapt `rag_api.py` to your own RAG system

**Advanced:**
1. `01_Production_Checklist.ipynb`
2. Add Docker + CI/CD pipeline
3. See `6_evaluation/` for adding eval logging to the API

## 🔗 What's Next?

- **`6_evaluation/`** — instrument your API to log evaluation metrics automatically
- **`8_case_studies/`** — see deployed RAG patterns for specific use cases

## 🔧 Installation

```bash
pip install fastapi uvicorn pydantic python-multipart
```

## 🤝 Contributing

Found an issue or want to add a notebook? Open an issue or PR!

---

**Remember:** Production RAG is mostly engineering, not AI. Treat it like any other API! 🚀
