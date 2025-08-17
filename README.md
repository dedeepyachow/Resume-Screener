AI-Powered Resume Screener
Project Overview: This project is a command-line tool for a modern, semantic-based resume screening system. Unlike traditional keyword-based tools, this application leverages advanced Natural Language Processing (NLP) techniques and a vector database to analyze the meaning and context of both resumes and job descriptions. The system efficiently ranks candidates by relevance, providing a powerful tool for recruiters and hiring managers.

Core Features:

Semantic Search: Utilizes a pre-trained sentence-transformers model (all-MiniLM-L6-v2) to convert resumes and job descriptions into high-dimensional vectors. This allows the system to understand the semantic similarity between skills and requirements.

High-Performance Indexing: Employs FAISS to create a lightning-fast vector search index, enabling efficient searching across large datasets of resumes.

Command-Line Interface: A simple command-line interface allows a user to paste a job description and receive a ranked list of the most relevant resumes.

Technology Stack:

Languages: Python

Libraries: sentence-transformers, faiss-cpu, numpy, python-docx

Getting Started:

Clone this repository.

Install the required packages:

Bash

pip install -r requirements.txt
Run the preprocessing, embedding, and indexing scripts in the following order:

Bash

python pre_process.py
python generate_embeddings.py
python build_index.py
Launch the search engine:

Bash

python search_engine.py
