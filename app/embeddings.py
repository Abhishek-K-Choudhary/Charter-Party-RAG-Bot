from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(chunks, embeddings)