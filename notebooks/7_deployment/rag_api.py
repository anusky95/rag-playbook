from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# --- Setup ---
app = FastAPI(title="My RAG API")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Knowledge base (in production: load from a database or vector store)
documents = [
    "RAG combines retrieval with LLM generation.",
    "Embeddings convert text into vectors for similarity search.",
    "Chunking splits long documents into smaller pieces.",
]
doc_embeddings = model.encode(documents)

# --- Request/Response models ---
class Question(BaseModel):
    question: str
    top_k: int = 2  # How many docs to retrieve (optional, default 2)

class Answer(BaseModel):
    answer: str
    sources: list[str]

# --- Endpoints ---
@app.get("/")
def health_check():
    return {"status": "ok", "docs": len(documents)}

@app.post("/ask", response_model=Answer)
def ask(body: Question):
    # 1. Embed the question
    q_emb = model.encode(body.question)

    # 2. Find relevant docs
    scores = cosine_similarity([q_emb], doc_embeddings)[0]
    top_idx = np.argsort(scores)[::-1][:body.top_k]
    sources = [documents[i] for i in top_idx]

    # 3. (Would call LLM here with sources as context)
    answer = f"Based on the context: {sources[0]}"

    return Answer(answer=answer, sources=sources)