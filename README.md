# AI-Powered Resume Screener

## Project Overview

This project is a command-line tool for a modern, semantic-based resume screening system. Unlike traditional keyword-based tools, this application leverages advanced Natural Language Processing (NLP) techniques and a vector database to analyze the meaning and context of both resumes and job descriptions. The system efficiently ranks candidates by relevance, providing a powerful tool for recruiters and hiring managers.

## Features

-   **Semantic Search:** Utilizes a pre-trained `sentence-transformers` model (`all-MiniLM-L6-v2`) to convert resumes and job descriptions into high-dimensional vectors. This allows the system to understand the semantic similarity between skills and requirements.
-   **High-Performance Indexing:** Employs **FAISS** to create a lightning-fast vector search index, enabling efficient searching across large datasets of resumes.
-   **Command-Line Interface:** A simple command-line interface allows a user to paste a job description and receive a ranked list of the most relevant resumes.

## Technology Stack

### Languages
-   Python

### Libraries
-   `sentence-transformers`
-   `faiss-cpu`
-   `numpy`
-   `python-docx`

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

-   Python 3.7 or higher
-   `pip` package manager

### Installation

1.  Clone this repository to your local machine:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  Install all the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  **Run the preprocessing script** to extract and clean text from the resumes.
    ```bash
    python pre_process.py
    ```

2.  **Generate vector embeddings** for the cleaned resume text.
    ```bash
    python generate_embeddings.py
    ```

3.  **Build the FAISS index** to prepare for efficient searching.
    ```bash
    python build_index.py
    ```

4.  **Launch the search engine** and input your job description when prompted.
    ```bash
    python search_engine.py
    ```
    The script will then output a ranked list of the most relevant resumes.
