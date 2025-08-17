import numpy as np
import json
import faiss

def load_data(embeddings_file, metadata_file):
    """Loads embeddings and metadata from files."""
    embeddings = np.load(embeddings_file)
    with open(metadata_file, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    return embeddings, list(metadata.keys())

def build_and_save_index(embeddings_file, metadata_file, index_file, filenames_file):
    """
    Loads embeddings and builds a FAISS index, then saves both the index and filenames.
    """
    print("Loading data...")
    resume_embeddings, resume_filenames = load_data(embeddings_file, metadata_file)
    print("Data loaded.")
    
    d = resume_embeddings.shape[1]
    
    print(f"Creating a FAISS index with dimension {d}...")
    index = faiss.IndexFlatL2(d)
    
    print(f"Adding {resume_embeddings.shape[0]} vectors to the index...")
    index.add(resume_embeddings)
    
    # Save the FAISS index
    faiss.write_index(index, index_file)
    
    # Save the filenames to a JSON file
    with open(filenames_file, "w") as f:
        json.dump(resume_filenames, f)
        
    print(f"Index successfully built and saved to {index_file}.")
    print(f"Filenames saved to {filenames_file}.")

if __name__ == "__main__":
    build_and_save_index(
        "resume_embeddings.npy", 
        "cleaned_resumes.json", 
        "resume_index.faiss", 
        "resume_filenames.json"
    )