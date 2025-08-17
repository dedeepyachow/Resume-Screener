import os
from docx import Document
import json
import re
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Define the path to your Resumes folder
resumes_folder_path = "Resumes"
stop_words = set(stopwords.words('english'))

def clean_text(text):
    """
    Performs a series of text cleaning operations with a focus on resumes.
    """
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove common resume headings and irrelevant sections
    # This pattern matches common headings and the text that follows them.
    text = re.sub(r'professional summary|technical skills|professional experience|responsibilities|environment|description', '', text)
    
    # 3. Remove dates, locations, and other unique identifiers
    text = re.sub(r'\w{3}\'\d{2}\s*[\u2013-]\s*till date|\w{3}\'\d{2}\s*[\u2013-]\s*\w{3}\'\d{2}', '', text)
    text = re.sub(r'[a-zA-Z]+, [a-zA-Z]{2}', '', text) # Simple pattern for cities/states like 'Stamford, CT'
    
    # 4. Remove URLs, email addresses, and other non-essential info
    text = re.sub(r'http\S+|www\S+|@\S+|[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '', text)
    
    # 5. Remove numbers and punctuation
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # 6. Remove newlines and extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # 7. Tokenize the text
    tokens = word_tokenize(text)
    
    # 8. Remove stop words
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # 9. Join the tokens back into a single string
    cleaned_text = " ".join(filtered_tokens)
    
    return cleaned_text

def extract_text_from_docx(file_path):
    """
    Extracts all text from a single .docx file.
    """
    document = Document(file_path)
    full_text = []
    for paragraph in document.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

def process_resumes_folder(folder_path):
    """
    Goes through the folder, extracts text from each .docx file,
    and returns a dictionary of file names and their cleaned text.
    """
    resumes_data = {}
    
    # Get a list of all files in the folder
    all_files = os.listdir(folder_path)
    
    # Filter for only .docx files
    docx_files = [f for f in all_files if f.endswith('.docx')]
    
    for file_name in docx_files:
        print(f"Processing {file_name}...")
        file_path = os.path.join(folder_path, file_name)
        
        # Extract the text from the docx file
        raw_text = extract_text_from_docx(file_path)
        
        cleaned_text = clean_text(raw_text)

        resumes_data[file_name] = raw_text
        
    return resumes_data

def save_to_json(data, filename):
    """Saves a dictionary to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
# Run the functions
resumes_data_cleaned = process_resumes_folder("Resumes")
save_to_json(resumes_data_cleaned, "cleaned_resumes.json")
print("Cleaned resume data saved to cleaned_resumes.json")
