# 🎯 Tokenization - The Foundation of RAG

Welcome to the **ULTIMATE** tokenization guide! This folder contains everything you need to master tokenization for RAG systems.

## 📚 What You'll Learn

Tokenization is the **first critical step** in any NLP/RAG pipeline. You'll learn:
- How text is converted to numbers (tokens)
- Different tokenization algorithms and when to use each
- How to chunk documents for retrieval
- Production-ready implementations

## 🗂️ Notebooks (In Order)

### Core Concepts
1. **`00_Tokenization_Overview.ipynb`** ⭐ START HERE
   - What is tokenization and why it matters
   - Types of tokenization methods
   - Impact on RAG systems
   - Quick reference guide

### Fundamental Methods
2. **`01_Word_Tokenization.ipynb`**
   - Word-level tokenization basics
   - Building vocabularies
   - Pros/cons for RAG
   - When (not) to use it

3. **`05_Character_Tokenization.ipynb`**
   - Character-level basics
   - Vocabulary analysis
   - Use cases (spell checking)
   - Why modern RAG avoids it

### Modern Subword Methods (MOST IMPORTANT!)
4. **`02_Subword_Tokenization_BPE.ipynb`** 🔥
   - Byte Pair Encoding (BPE)
   - Used by: GPT-2, GPT-3, GPT-4
   - Training your own BPE
   - Production examples

5. **`03_WordPiece_Tokenization.ipynb`** 🔥
   - WordPiece algorithm
   - Used by: BERT, DistilBERT, E5
   - The ## notation explained
   - Perfect for embeddings

6. **`04_SentencePiece_Tokenization.ipynb`** 🔥
   - Language-agnostic tokenization
   - Used by: T5, mT5, ALBERT
   - Multilingual RAG
   - The ▁ character explained

### Document Processing
7. **`06_Sentence_Tokenization.ipynb`** 📄
   - Essential for RAG chunking
   - Document splitting strategies
   - Chunking with overlap
   - Production pipelines

### Quick Reference
8. **`07_Tokenization_Comparison_Guide.ipynb`** 📋
   - Side-by-side comparison
   - Decision tree
   - Code templates
   - Production checklist

## 🚀 Quick Start

```python
# For RAG with BERT embeddings (MOST COMMON)
from transformers import BertTokenizer
from nltk.tokenize import sent_tokenize

# Document chunking
sentences = sent_tokenize(document)

# Tokenization
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize(text)
```

## 🎯 Quick Decision Guide

**Choose your tokenizer based on your model:**

| Your Model | Use This Tokenizer | Notebook |
|------------|-------------------|----------|
| BERT, MiniLM, E5 | WordPiece | 03 |
| GPT-2, GPT-3, GPT-4 | BPE | 02 |
| T5, mT5, ALBERT | SentencePiece | 04 |
| Document chunking | Sentence | 06 |
| Multilingual | SentencePiece | 04 |

## 📊 Comparison at a Glance

| Method | Vocab | Unknown Words | Best For |
|--------|-------|--------------|----------|
| Word-level | 50k-1M+ | ❌ | Basic search |
| Character | 100-300 | ✅ | Spell check |
| **BPE** | **50k** | **✅** | **GPT models** |
| **WordPiece** | **30k** | **✅** | **BERT models** |
| **SentencePiece** | **32k** | **✅** | **Multilingual** |
| Sentence | N/A | N/A | Document chunking |

## 💡 Key Takeaways

1. **Subword tokenization wins** - BPE, WordPiece, and SentencePiece are used in all modern models
2. **Match your model** - Use the same tokenizer as your embedding/generation model
3. **Sentence-based chunking** - Essential for RAG retrieval quality
4. **Token limits matter** - Different models have different context windows

## 🔧 Installation

```bash
# Install all required packages
pip install transformers tokenizers sentencepiece nltk spacy tiktoken

# Download language models
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt')"
```

## 📖 Recommended Path

**Beginner:**
1. Start with `00_Tokenization_Overview.ipynb`
2. Read `01_Word_Tokenization.ipynb` for basics
3. Master `02_Subword_Tokenization_BPE.ipynb`
4. Learn `06_Sentence_Tokenization.ipynb` for RAG

**Intermediate:**
1. Deep dive into `03_WordPiece_Tokenization.ipynb`
2. Explore `04_SentencePiece_Tokenization.ipynb`
3. Use `07_Tokenization_Comparison_Guide.ipynb` as reference

**Advanced:**
- Train custom tokenizers
- Optimize chunking strategies
- Implement domain-specific tokenization

## 🎓 Production Checklist

Before deploying your RAG system:

- [ ] Choose tokenizer matching your embedding model
- [ ] Choose tokenizer matching your LLM
- [ ] Implement sentence-based chunking
- [ ] Add 1-2 sentence overlap in chunks
- [ ] Verify token counts fit model limits
- [ ] Test on your domain's documents
- [ ] Handle edge cases (URLs, emails, abbreviations)
- [ ] Cache tokenization results for speed

## 🌟 Common Patterns

### Pattern 1: English RAG (BERT Embeddings + GPT Generation)
```python
from nltk.tokenize import sent_tokenize
from transformers import BertTokenizer, GPT2Tokenizer

# Chunking
chunks = sent_tokenize(document)

# Embedding
bert_tok = BertTokenizer.from_pretrained('bert-base-uncased')
embeddings = model.encode(chunks, tokenizer=bert_tok)

# Generation
gpt_tok = GPT2Tokenizer.from_pretrained('gpt2')
tokens = gpt_tok.encode(prompt)
```

### Pattern 2: Multilingual RAG
```python
from transformers import T5Tokenizer

# One tokenizer for everything
tokenizer = T5Tokenizer.from_pretrained('google/mt5-base')
```

### Pattern 3: Production RAG Pipeline
```python
from nltk.tokenize import sent_tokenize
from transformers import AutoTokenizer

def prepare_documents(docs, max_tokens=512):
    tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
    
    all_chunks = []
    for doc in docs:
        # Sentence-based chunking
        sentences = sent_tokenize(doc)
        
        # Group into token-limited chunks
        chunk = []
        tokens = 0
        
        for sent in sentences:
            sent_tokens = len(tokenizer.encode(sent))
            if tokens + sent_tokens > max_tokens:
                all_chunks.append(' '.join(chunk))
                chunk = [sent]
                tokens = sent_tokens
            else:
                chunk.append(sent)
                tokens += sent_tokens
        
        if chunk:
            all_chunks.append(' '.join(chunk))
    
    return all_chunks
```

## 🔗 What's Next?

After mastering tokenization, move to:
- **`2_retrieval/`** - Build the retrieval system
- **`3_search_techniques/`** - Advanced search methods
- **`4_generation/`** - LLM integration
- **`5_advanced_rag/`** - Production optimization

## 📝 Additional Resources

- [HuggingFace Tokenizers](https://huggingface.co/docs/tokenizers/)
- [SentencePiece GitHub](https://github.com/google/sentencepiece)
- [NLTK Documentation](https://www.nltk.org/)
- [spaCy Tokenization](https://spacy.io/usage/linguistic-features#tokenization)

## 🤝 Contributing

Found an issue or want to add a notebook? Open an issue or PR!

---

**Remember:** Tokenization is the foundation. Master it, and everything else becomes easier! 🚀

Ready? Start with `00_Tokenization_Overview.ipynb`!