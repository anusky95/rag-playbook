# 🏛️ Industry Verticals - Domain-Specific RAG

RAG in regulated industries isn't just about accuracy — it's about compliance, liability, and trust. This folder covers how RAG must adapt for legal, medical, and financial domains.

## 🎯 Why Domain-Specific RAG Matters

```
General RAG:  "Here's what I found about treatment options."
Medical RAG:  "Based on Level A evidence (RCT): [citation]. Consult your physician."

General RAG:  "The contract says X."
Legal RAG:    "Source [§3.2]: [exact quote]. This is not legal advice."
```

Each industry has different requirements for citation format, confidence expression, disclaimers, and what the system must never say.

## 📚 Notebooks

1. **`00_RAG_for_Legal.ipynb`** ⚖️
   - Mandatory source citations with exact quotes
   - Conservative, hedged language
   - Jurisdiction awareness (laws vary by location)
   - High precision threshold — better to say "I don't know" than guess
   - What the system must never do: give legal advice, interpret intent
   - Compliance checklist for legal AI products

2. **`01_RAG_for_Medical.ipynb`** 🏥
   - Evidence levels: Level A (RCT), Level B (cohort), Level C (expert opinion)
   - Weight retrieved documents by evidence quality, not just relevance
   - Show evidence level alongside every claim
   - Mandatory: "This is not medical advice. Consult a qualified physician."
   - Drug interaction and contraindication flags
   - Compliance checklist for clinical AI products

3. **`02_RAG_for_Finance.ipynb`** 💰
   - Preserve exact numbers — never round or paraphrase financial figures
   - Always show time period: FY2024 vs FY2023 vs TTM
   - Filter by recency: stale financial data can be materially misleading
   - Required disclaimer: "This is not investment advice."
   - Regulatory citations (SEC filings, prospectuses) vs news vs analysis
   - Compliance checklist for finance AI products

## 📊 Domain Requirements at a Glance

| Requirement | Legal | Medical | Finance |
|-------------|-------|---------|---------|
| Exact source quotes | Required | Required | Required |
| Evidence/confidence level | Optional | Required | Optional |
| Time-sensitivity | High | High | Critical |
| Precision threshold | High | Very high | High |
| "Not advice" disclaimer | Required | Required | Required |
| Never speculate | Must | Must | Must |

## 💡 Key Patterns

### Legal: Citation-First Prompting
```python
system_prompt = """You are a legal research assistant.
RULES:
- Cite the exact section (e.g., §3.2(a)) for every claim
- Use exact quotes from the source text
- Always include: "This is not legal advice."
- If the answer depends on jurisdiction, say so explicitly
- If you are uncertain, say "I cannot determine this from the provided sources."
"""
```

### Medical: Evidence Weighting
```python
def weight_by_evidence(docs):
    evidence_weights = {"RCT": 1.0, "cohort": 0.8, "expert": 0.5, "case_report": 0.3}
    return sorted(docs, key=lambda d: evidence_weights.get(d.study_type, 0.4), reverse=True)
```

### Finance: Number Preservation
```python
system_prompt = """You are a financial research assistant.
RULES:
- Never round, paraphrase, or restate financial figures — use exact numbers from sources
- Always cite the time period (e.g., Q3 FY2024, TTM as of March 2025)
- Always include: "This is not investment advice."
- If data is older than 90 days, flag it as potentially stale
"""
```

## 📖 Learning Path

**Entering a regulated domain:**
1. Read the compliance checklist at the end of the relevant notebook
2. Adapt the system prompt and retrieval filters for your domain
3. Get legal/compliance review before deploying in production

**Building a general-purpose regulated RAG system:**
1. `00_RAG_for_Legal.ipynb` — strictest citation requirements
2. `01_RAG_for_Medical.ipynb` — evidence-level weighting
3. `02_RAG_for_Finance.ipynb` — time-sensitivity and number precision

## 🎓 Production Checklist (All Domains)

- [ ] "Not advice" disclaimer in every response
- [ ] Source citations with exact quotes, not paraphrases
- [ ] Confidence/evidence level shown where applicable
- [ ] Recency filter applied (financial and medical data especially)
- [ ] Response reviewed by domain expert before going live
- [ ] Legal/compliance sign-off on system prompt and disclaimers
- [ ] Out-of-scope query handling tested
- [ ] Monitoring for responses that omit required disclaimers

## 🔗 What's Next?

- **`7_deployment/`** — deploy compliant RAG with audit logging
- **`6_evaluation/`** — evaluate faithfulness (critical in regulated domains)
- **`8_case_studies/`** — general patterns you can adapt before adding domain constraints

## 🔧 Installation

```bash
pip install sentence-transformers anthropic
```

## ⚠️ Important Disclaimer

The notebooks in this folder are for **educational purposes only**. Before deploying AI in legal, medical, or financial contexts, consult qualified professionals and review applicable regulations in your jurisdiction.

## 🤝 Contributing

Found an issue or want to add a vertical? Open an issue or PR!

---

**Remember:** In regulated industries, "I don't know" is always safer than a confident wrong answer. Design for caution! 🏛️
