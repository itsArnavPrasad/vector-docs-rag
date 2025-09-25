from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import os
from sqlalchemy.orm import Session
from database import PDFChunk, SessionLocal, init_db
from pdf_utils import extract_text, chunk_text
from embeddings import build_faiss_index, query_faiss
from rag_gemma import generate_answer

# Initialize DB
print("Initializing database...")
init_db()

app = FastAPI()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def save_file(file: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    print(f"Saved file to {file_path}")
    return file_path

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    file_path = save_file(file)
    
    text = extract_text(file_path)
    
    chunks = chunk_text(text, chunk_size=500)
    print(f"Extracted {len(chunks)} chunks from the PDF.")

    # Save chunks to DB
    db: Session = SessionLocal()
    for i, chunk in enumerate(chunks):
        pdf_chunk = PDFChunk(
            filename=file.filename,
            chunk_text=chunk,
            chunk_number=i+1,
            page_start=None,  # Optional: you can calculate page range
            page_end=None
        )
        db.add(pdf_chunk)
    print(f"Saved {len(chunks)} chunks to the database.")
    db.commit()
    db.close()
    
    return {"filename": file.filename, "num_chunks": len(chunks)}


@app.post("/build-index")
async def build_index():
    build_faiss_index()
    return {"status": "FAISS index built successfully."}

@app.get("/query")
async def query_document(q: str = Query(...), k: int = 3):
    results = query_faiss(q, k)
    return {"query": q, "results": results}

@app.get("/rag-answer")
async def rag_answer(q: str = Query(...), top_k: int = 3):
    answer = generate_answer(q, top_k)
    return {"query": q, "answer": answer}

@app.get("/list-files")
async def list_files():
    files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(".pdf")]
    return {"files": files}