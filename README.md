📄 Charter Party RAG Bot

A Retrieval-Augmented Generation (RAG) application for analyzing Charter Party contracts using Large Language Models.

This tool allows users to upload a Charter Party PDF and ask natural-language questions such as:

“What are the demurrage terms?”

“Is there a war risk clause?”

“What are the arbitration provisions?”

The system retrieves relevant clauses from the contract and generates answers strictly grounded in the document text.

🚀 Overview

Manual review of Charter Party contracts can be time-consuming and repetitive.
This project demonstrates how RAG architecture can automate clause discovery and contract Q&A while maintaining traceability and legal accuracy.

The application:

Extracts text from uploaded PDFs

Splits documents into semantic chunks

Creates vector embeddings

Performs similarity search

Generates grounded answers using an LLM

Displays supporting source clauses and page references

🧠 Architecture
PDF Upload
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Store (FAISS)
   ↓
Similarity Retrieval
   ↓
LLM (temperature = 0)
   ↓
Answer + Source Clauses


The model is configured to:

Answer strictly from retrieved context

Avoid hallucinations

Return “Not specified in the contract.” when information is missing

🛠️ Tech Stack

Python

LangChain

Streamlit

FAISS (Vector Database)

OpenAI API

python-dotenv

📂 Project Structure
charter-party-rag-bot/
│
├── app/
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── prompts.py
│   └── utils.py
│
├── tests/
│   └── test_basic.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

⚙️ Installation
1. Clone the repository
git clone https://github.com/yourusername/charter-party-rag-bot.git
cd charter-party-rag-bot

2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

3. Install dependencies
pip install -r requirements.txt

🔑 Environment Setup

Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key_here


Do not commit your .env file.

▶️ Run the Application
streamlit run app/main.py


Then open:

http://localhost:8501


Upload a Charter Party PDF and begin querying the document.