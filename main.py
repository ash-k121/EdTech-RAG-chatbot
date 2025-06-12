from app.ingestion.ingest import ingest_docs
from app.embedding.embed import create_vector_db

def main():
    docs = ingest_docs("docs/sample.pdf")
    create_vector_db(docs)

if __name__ == "__main__":
    main()
