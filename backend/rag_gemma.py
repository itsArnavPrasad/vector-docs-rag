from embeddings import query_faiss
from ollama import chat


def generate_answer(query, top_k=5):
    """
    RAG: Retrieve top-k chunks from FAISS, feed to LLM
    """
    # Retrieve top-k relevant chunks (implement query_faiss function as needed)
    chunks = query_faiss(query, k=top_k)
    print(f"Retrieved {len(chunks)} relevant chunks from FAISS.")

    # Format context with source information
    context = "\n".join([f"{i+1}. ({c['filename']}) {c['chunk_text']}" for i, c in enumerate(chunks)])
    
    # Construct prompt
    prompt = f"Answer the question based on the following context, these are chunks retrived from FAISS search on the RAG PDFs:\n{context}\n\nQuestion: {query}\nAnswer:"

    # Generate response
    response = chat(model="gemma3:1b", messages=[{"role": "user", "content": prompt}])
    print("LLM Response:", response)
    return response['message']['content']
