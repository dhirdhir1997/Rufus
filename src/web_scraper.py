from bs4 import BeautifulSoup
from keybert import KeyBERT
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize
from datetime import datetime
from .nlp import filter_content
from .utils import save_to_json, resilient_request, is_relevant, clean_text

kw_model = KeyBERT()
vectorizer = TfidfVectorizer()

def simple_crawl(url):
    """
    Fetch and parse the content of the URL as HTML.
    """
    response = resilient_request(url)
    if response:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to retrieve content from {url}")
        return None

def crawl_links(soup, base_url, keywords):
    """
    Crawl the page links and return those that are relevant to the given keywords.
    """
    vectorizer.fit(keywords)
    links = [a['href'] for a in soup.find_all('a', href=True) if is_relevant(a.text, keywords)]

    relevant_links = []
    for link in links[:5]:  # Limit to 5 links
        full_url = requests.compat.urljoin(base_url, link)
        try:
            content = simple_crawl(full_url).get_text()
            tfidf_matrix = vectorizer.transform([content])
            keyword_vector = vectorizer.transform([' '.join(keywords)])
            similarity = cosine_similarity(tfidf_matrix, keyword_vector).flatten()[0]
            if similarity >= 0.3:
                relevant_links.append(full_url)
        except Exception:
            continue

    return relevant_links

def scrape_website(url, instructions):
    """
    Scrapes a website and extracts relevant information based on the given instructions.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    soup = simple_crawl(url)
    if not soup:
        return None

    keywords = kw_model.extract_keywords(instructions, top_n=10)
    keyword_list = [k for k, _ in keywords]
    links = crawl_links(soup, url, keyword_list)

    documents = []
    for link in links:
        link_soup = simple_crawl(link)
        if link_soup:
            filtered_content = filter_content(link_soup.text, keyword_list)
            cleaned_content = clean_text(" ".join(filtered_content))
            sentences = sent_tokenize(cleaned_content)
            documents.append({"url": link, "content": sentences})

    output_data = {"timestamp": timestamp, "results": documents}
    save_to_json(output_data, "output.json")
    return output_data
