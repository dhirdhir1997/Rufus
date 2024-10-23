### Handling Dynamic Web Pages:
- **Challenge:** Many websites use JavaScript to load content dynamically, which cannot be easily scraped with traditional HTML parsing libraries like BeautifulSoup.
- **Solution:** I integrated Selenium into the web scraper to handle JavaScript rendering and dynamic content loading. This allowed the scraper to fully render and capture complex web pages.

### Relevant Content Extraction:
- **Challenge:** Extracting only the relevant parts of a webpage based on user instructions was difficult, especially when pages contain vast amounts of data not relevant to the query.
- **Solution:** I employed NLP-based keyword extraction using KeyBERT to match the user's query to the most relevant content. This, combined with Spacy and transformer models, helped to identify and score sentences that matched the user’s instructions.

### Scalability:
- **Challenge:** Ensuring that the scraper was scalable and could handle large websites and multiple requests without breaking.
- **Solution:** I implemented robust error handling and retry mechanisms using custom utility functions in utils.py, making the scraper resilient to network errors, broken links, or changing web structures.

### Testing and Validation:
- **Challenge:** Ensuring the scraper works across different types of websites with varied structures.
- **Solution:** I created unit tests using Python’s unittest framework to validate the core functionality of the scraper, including handling both static and dynamic web pages, and correctly filtering content based on user instructions.
