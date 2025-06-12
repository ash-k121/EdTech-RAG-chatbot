import streamlit as st
# import sys
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.llm_pipeline.qa import get_qa_chain

# from pathlib import Path
# sys.path.append(str(Path(__file__).parent.parent.parent))
from app.llm_pipeline.qa import get_qa_chain
# from ..llm_pipeline.qa import get_qa_chain
st.set_page_config(page_title="EdTech RAG Assistant", page_icon="📘")
st.title("📘 EdTech Document Chatbot")
st.markdown("Ask questions based on your uploaded textbook or notes.")

from app.llm_pipeline.qa import get_qa_chain

db, chain = get_qa_chain()  

query = st.text_input("Enter your question:")

if query:
    with st.spinner("Thinking..."):
        docs = db.similarity_search(query)       
        result = chain.run(input_documents=docs, question=query) 
    st.success(result)
