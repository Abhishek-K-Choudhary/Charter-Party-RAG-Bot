import os
from dotenv import load_dotenv
import logging


def load_environment():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")

    return api_key


def clean_text(text: str) -> str:
    return " ".join(text.split())


def format_sources(source_documents):
    formatted_sources = []

    for i, doc in enumerate(source_documents):
        formatted_sources.append({
            "clause_number": i + 1,
            "content": doc.page_content.strip(),
            "metadata": doc.metadata
        })

    return formatted_sources


def extract_page_numbers(source_documents):
    pages = []
    for doc in source_documents:
        if "page" in doc.metadata:
            pages.append(doc.metadata["page"] + 1)  # human-readable
    return sorted(list(set(pages)))


# Logging setup
logging.basicConfig(level=logging.INFO)

def log_event(message: str):
    logging.info(f"[CharterRAG] {message}")