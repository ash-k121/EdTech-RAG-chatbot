# app/embedding/embed.py
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_db(docs):
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embedder)
    db.save_local("faiss_index")
    print("✅ FAISS index saved to 'faiss_index/'")
