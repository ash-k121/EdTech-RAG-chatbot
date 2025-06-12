
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms.ollama import Ollama
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

def get_qa_chain():
    
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    
    db = FAISS.load_local(
        folder_path="faiss_index",
        embeddings=embedder,
        allow_dangerous_deserialization=True
    )

    llm = Ollama(model="tinyllama") 

    
    template_text = (
        "You are an AI tutor. Use the following context to answer the student's question.\n\n"
        "Context:\n{context}\n\n"
        "Question:\n{question}\n\n"
        "Answer:"
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template_text
    )

    
    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

    return db, chain
