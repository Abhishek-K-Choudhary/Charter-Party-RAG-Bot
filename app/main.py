import streamlit as st
from rag_pipeline import get_answer
from utils import (
    load_environment,
    format_sources,
    extract_page_numbers,
    log_event
)

# Load API key
load_environment()

st.set_page_config(page_title="Charter Party RAG Bot")

st.title("📄 Charter Party RAG Assistant")
st.write("Upload a Charter Party contract and ask legal questions.")

uploaded_file = st.file_uploader("Upload Charter Party PDF", type=["pdf"])
question = st.text_input("Ask a question (e.g. What are the demurrage terms?)")

if uploaded_file and question:
    with st.spinner("Analyzing contract..."):
        try:
            response = get_answer(uploaded_file, question)

            st.subheader("Answer")
            st.write(response["result"])

            formatted_sources = format_sources(response["source_documents"])
            pages = extract_page_numbers(response["source_documents"])

            st.info(f"Referenced Pages: {pages}")

            with st.expander("Source Clauses"):
                for source in formatted_sources:
                    st.markdown(f"**Clause {source['clause_number']}**")
                    st.write(source["content"])

        except Exception as e:
            log_event(f"Error: {str(e)}")
            st.error("An error occurred. Check logs.")