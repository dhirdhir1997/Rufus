import spacy
from .utils import calculate_sentence_similarity

nlp = spacy.load('en_core_web_sm')

def filter_content(content, keywords):
    """
    Filter the content by extracting sentences that are similar to the provided keywords.
    """
    doc = nlp(content)
    sentences = [sent.text for sent in doc.sents]
    filtered_sentences = []
    
    for sentence in sentences:
        max_similarity = 0
        for keyword in keywords:
            max_similarity = max(max_similarity, calculate_sentence_similarity(keyword, sentence))
        
        if max_similarity > 0.8:
            filtered_sentences.append(sentence)
    
    return filtered_sentences
