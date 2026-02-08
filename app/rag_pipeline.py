from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

from app.pdf_loader import load_pdf
from app.text_splitter import split_documents
from app.embeddings import create_vectorstore
from app.prompts import SYSTEM_PROMPT
from app.utils import log_event


def build_qa_chain(uploaded_file):
    log_event("Loading PDF...")
    documents = load_pdf(uploaded_file)

    log_event("Splitting into chunks...")
    chunks = split_documents(documents)

    log_event("Creating vector store...")
    vectorstore = create_vectorstore(chunks)

    prompt = PromptTemplate(
        template=SYSTEM_PROMPT + "\n\nContext:\n{context}\n\nQuestion:\n{question}",
        input_variables=["context", "question"]
    )

    log_event("Building QA chain...")
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True,
    )

    return qa_chain


def get_answer(uploaded_file, question):
    qa_chain = build_qa_chain(uploaded_file)

    log_event(f"Processing question: {question}")
    response = qa_chain(question)

    return response