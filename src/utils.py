import re
import json
import requests
import torch
from transformers import AutoTokenizer, AutoModel

# Load sentence transformer model
model_name = "sentence-transformers/all-MiniLM-L6-v2"
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def resilient_request(url, retries=3):
    """
    Perform a resilient HTTP GET request with retries.
    """
    for _ in range(retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response
        except requests.RequestException:
            continue
    return None

def save_to_json(data, filename='output.json'):
    """
    Save the data to a JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def is_relevant(link_text, keywords):
    """
    Determine if the link text is relevant to the given keywords.
    """
    score = sum(keyword.lower() in link_text.lower() for keyword in keywords)
    return score > 0

def calculate_sentence_similarity(sentence1, sentence2):
    """
    Calculate similarity between two sentences using pre-trained transformer model.
    """
    inputs1 = tokenizer(sentence1, return_tensors="pt")
    inputs2 = tokenizer(sentence2, return_tensors="pt")

    embeddings1 = model(**inputs1).last_hidden_state[:, 0, :]
    embeddings2 = model(**inputs2).last_hidden_state[:, 0, :]

    similarity = torch.cosine_similarity(embeddings1, embeddings2)
    return similarity.item()

def clean_text(text):
    """
    Clean text by removing unnecessary whitespace and control characters.
    """
    text = re.sub(r'\s+', ' ', text).strip()
    return re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
