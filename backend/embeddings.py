import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from database import PDFChunk, SessionLocal

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

FAISS_DIR = "faiss_index"
os.makedirs(FAISS_DIR, exist_ok=True)
FAISS_PATH = os.path.join(FAISS_DIR, "pdf_chunks.index")

# Create or load FAISS index
def load_or_create_index(dim=384):
    if os.path.exists(FAISS_PATH):
        index = faiss.read_index(FAISS_PATH)
    else:
        index = faiss.IndexFlatL2(dim)
    return index

index = load_or_create_index()

# Function to compute embeddings from DB and add to FAISS
def build_faiss_index():
    db = SessionLocal()
    chunks = db.query(PDFChunk).all()
    texts = [c.chunk_text for c in chunks]
    
    if not texts:
        print("No chunks found in DB to embed.")
        return
    
    embeddings = model.encode(texts, convert_to_numpy=True)
    
    # Clear existing index and add new embeddings
    global index
    if index.ntotal > 0:
        index.reset()
    index.add(embeddings)
    
    # Save index
    faiss.write_index(index, FAISS_PATH)
    print(f"FAISS index built with {len(texts)} embeddings.")

# Function to query top-k similar chunks
def query_faiss(query, k=5):
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, k)
    
    db = SessionLocal()
    results = []
    for idx in indices[0]:
        if idx < 0:
            continue
        chunk = db.query(PDFChunk).offset(idx).first()
        results.append({"filename": chunk.filename, "chunk_text": chunk.chunk_text})
    return results
