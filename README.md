
![image](https://github.com/user-attachments/assets/bb9687c0-85e4-4adb-987c-1cce988b2432)


EdTechBot is a smart assistant that helps students interactively learn from their own textbooks and notes. Just upload your academic material, ask questions naturally, and get context-aware answers based on what you’ve uploaded — not from the internet.

It’s built on a Retrieval-Augmented Generation (RAG) architecture, combining semantic search with language models to deliver highly relevant responses.

Built With: LangChain • Sentence Transformers • FAISS • Streamlit • TinyLlama (via Ollama)

---

## Features

- Upload your own PDFs or notes to create a private, searchable knowledge base
- Retrieve relevant chunks using semantic similarity with Sentence Transformers + FAISS
- Get context-aware answers from a local LLM (TinyLlama via Ollama) or a cloud-hosted model like OpenAI or Hugging Face
- See exactly which text chunks were used to generate the answer
- Simple Streamlit-based user interface for real-time interaction
- Optional chat memory support for follow-up questions (LangChain memory modules)

---

## How It Works

1. Upload a document (PDF, TXT, or Markdown)
2. The document is split into smaller chunks and embedded using `all-MiniLM-L6-v2`
3. These embeddings are stored in a FAISS vector store
4. When a question is asked:
   - The top relevant chunks are retrieved based on similarity
   - A custom prompt combines those chunks with the user query
   - The prompt is passed to a local or hosted language model
5. The answer is displayed in the Streamlit interface, along with the referenced source content

---

## Tech Stack

| Layer         | Tools Used                              |
|---------------|------------------------------------------|
| Frontend      | Streamlit                                |
| Backend       | LangChain, Python                        |
| Embedding     | SentenceTransformers (MiniLM)            |
| Vector DB     | FAISS                                    |
| LLM Options   | TinyLlama (via Ollama), OpenAI, HF Hub   |
| Prompting     | LangChain QA Chain with context          |

---

## Getting Started (Local)

Clone the repository and install dependencies:

```bash
git clone https://github.com/ash-k121/EdTech-RAG-chatbot
cd EdTech-RAG-chatbot
pip install -r requirements.txt
streamlit run app.py
