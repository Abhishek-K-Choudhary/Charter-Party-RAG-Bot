from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from pdf_loader import load_pdf
from text_splitter import split_documents
from utils import log_event
from prompts import SYSTEM_PROMPT


def build_chain(uploaded_file):
    log_event("Loading PDF...")
    documents = load_pdf(uploaded_file)

    log_event("Splitting into chunks...")
    chunks = split_documents(documents)

    log_event("Creating vector store...")
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template(
        SYSTEM_PROMPT + "\n\nContext:\n{context}\n\nQuestion:\n{question}"
    )

    # LCEL RAG Pipeline
    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain


def get_answer(uploaded_file, question):
    chain = build_chain(uploaded_file)

    log_event(f"Processing question: {question}")

    response = chain.invoke(question)

    return {"result": response}