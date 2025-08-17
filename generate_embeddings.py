import json
import numpy as np
from sentence_transformers import SentenceTransformer

def load_from_json(filename):
    """Loads a dictionary from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_and_save_embeddings(cleaned_data_file, output_embeddings_file, model_name='all-MiniLM-L6-v2'):
    """Loads cleaned text, generates embeddings, and saves them to a file."""
    
    # Load the cleaned text data
    cleaned_resumes = load_from_json(cleaned_data_file)
    resume_texts = list(cleaned_resumes.values())
    
    # Load the pre-trained embedding model
    print(f"Loading SentenceTransformer model: {model_name}...")
    model = SentenceTransformer(model_name)
    
    # Generate embeddings
    print("Generating embeddings for resumes...")
    resume_embeddings = model.encode(resume_texts)
    
    # Save the embeddings
    np.save(output_embeddings_file, resume_embeddings)
    print(f"Embeddings saved to {output_embeddings_file}")
    
    return resume_embeddings, list(cleaned_resumes.keys())

if __name__ == "__main__":
    embeddings, filenames = generate_and_save_embeddings("cleaned_resumes.json", "resume_embeddings.npy")
    
    # You can inspect the results to see the shape of your embeddings
    print(f"\nShape of the embeddings: {embeddings.shape}")
    print(f"Number of resumes processed: {len(filenames)}")