# Biomedical Question Answering with RAG

**An end-to-end Retrieval-Augmented Generation (RAG) pipeline for biomedical question answering using the BioASQ dataset.**

This project demonstrates how to combine **dense embeddings**, **FAISS vector search**, **cross-encoder reranking**, and **LLM-based answer generation** for high-quality, context-aware responses in the biomedical domain.

---

## Features

* **RAG Pipeline:** Combines retrieval and generation for accurate question answering.
* **FAISS Vector Database:** ~40k biomedical passage embeddings for fast semantic search.
* **Domain-Specific Embeddings:** Uses `S-PubMedBERT-MS-MARCO` for improved biomedical relevance.
* **Cross-Encoder Reranker:** Refines top-k retrieved passages using `MS-MARCO MiniLM`.
* **LLM Integration:** Generates natural language answers via `Gemma3-1B` using the Ollama API.
* **Evaluation Metrics:** Reports **Recall@k** and **MRR** for retrieval performance.

---

## Results

| Model / Step                                       | Recall@5 | MRR   |
| -------------------------------------------------- | -------- | ----- |
| Baseline embeddings (all-MiniLM-L6-v2)             | 0.800    | 0.652 |
| Domain-specific embeddings (S-PubMedBERT-MS-MARCO) | 0.850    | 0.656 |
| + Cross-encoder reranker + LLM                     | 0.900    | 0.817 |

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/bio-rag.git
cd bio-rag
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Project Highlights

* Built a **RAG pipeline** for biomedical QA with Hugging Face datasets.
* Constructed a **FAISS vector database** with ~40k biomedical embeddings.
* Improved **retrieval metrics** using **domain-specific embeddings**.
* Added **cross-encoder reranking** to refine top-k passages.
* Integrated **Gemma3-1B LLM** for natural language answer generation.

---

## 🔗 References

* [BioASQ Dataset](http://bioasq.org/)
* [Sentence Transformers](https://www.sbert.net/)
* [FAISS](https://faiss.ai/)
* [Hugging Face Datasets](https://huggingface.co/docs/datasets/)
* [Ollama LLM](https://ollama.com/)
