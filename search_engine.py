import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer

# --- Load Pre-built Assets ---
print("Loading assets...")
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("resume_index.faiss")
with open("resume_filenames.json", "r") as f:
    resume_filenames = json.load(f)
print("Assets loaded successfully.\n")

# --- Define Search Function ---
def find_top_matches(job_description, k=5):
    """Finds the top k most relevant resumes."""
    query_vector = model.encode([job_description])
    distances, indices = index.search(query_vector, k)
    
    results = []
    for i in range(k):
        match_index = indices[0][i]
        match_filename = resume_filenames[match_index]
        score = 1 / (1 + distances[0][i]) # Simple inverse score
        results.append((match_filename, score))
        
    return results

# --- Main Program Execution ---
if __name__ == "__main__":
    print("Welcome to the AI-Powered Resume Screener!")
    print("Enter a job description to find the most relevant resumes. Type 'exit' to quit.")
    
    while True:
        job_description_input = input("\nEnter Job Description: ")
        
        if job_description_input.lower() == 'exit':
            break
            
        if not job_description_input.strip():
            print("Please enter a valid job description.")
            continue
            
        print("\nSearching for top matches...")
        top_resumes = find_top_matches(job_description_input, k=3)
        
        print("\n--- Top 3 Matching Resumes ---")
        for rank, (filename, score) in enumerate(top_resumes, 1):
            print(f"Rank {rank}: {filename}")
            print(f"  Relevance Score: {score:.4f}\n")