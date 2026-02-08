from langchain.document_loaders import PyPDFLoader
import tempfile
import os
from app.utils import clean_text


def load_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    loader = PyPDFLoader(temp_path)
    documents = loader.load()

    os.remove(temp_path)

    # Clean text
    for doc in documents:
        doc.page_content = clean_text(doc.page_content)

    return documents