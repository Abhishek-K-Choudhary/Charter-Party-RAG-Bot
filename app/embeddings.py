from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS


def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(chunks, embeddings)