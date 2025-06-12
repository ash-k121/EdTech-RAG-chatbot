# 🎓 EdTechBot – AI Tutor from PDF Notes

EdTechBot is an AI-powered question-answering app that lets students ask questions based on their uploaded study materials (e.g., textbooks, notes in PDF). It uses LangChain + FAISS + HuggingFace for semantic search and Ollama's lightweight LLMs (like `tinyllama`) for local, private, and offline-friendly responses.

![image](https://github.com/user-attachments/assets/bb9687c0-85e4-4adb-987c-1cce988b2432)

---

## 🚀 Features

- 📚 Ask questions from your own textbook/PDF
- 💬 Local LLM inference using [Ollama](https://ollama.com/)
- 🧠 Vector search using FAISS
- 🌐 Runs entirely offline after setup
- 🎯 Lightweight: works with ~4GB RAM using `tinyllama`

---

## 🛠️ Tech Stack

- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.com/) (`tinyllama`)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://huggingface.co/sentence-transformers)
- [Streamlit](https://streamlit.io/) for UI

---

## 🧪 How It Works

1. `main.py` reads a sample PDF (`docs/sample.pdf`)
2. Text is chunked and embedded using HuggingFace
3. Vector store is built and saved using FAISS
4. Streamlit app loads the vector DB and lets you ask questions
5. Ollama's local LLM (`tinyllama`) answers contextually

---

## 🧰 Local Setup

### 1. Install Ollama

Download & install from: https://ollama.com/download

Then run:
```bash
ollama run tinyllama
```
### 2. Run
streamlit app/ui/apps.py
