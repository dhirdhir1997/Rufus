## Rufus Case Study
Building Rufus – A Tool for Intelligent Web Data Extraction for LLMs.
The **Rufus Web Scraper** is an AI-powered tool designed to scrape web content from websites such as [North Carolina State University (NCSU)](https://www.ncsu.edu/) and extract relevant information based on user instructions. The tool leverages web scraping, natural language processing (NLP), and keyword extraction techniques to gather, filter, and present structured data in an easily understandable format.

## Features

- **Web Scraping**: Uses `BeautifulSoup` and `requests` to scrape static web pages.
- **Dynamic Content Handling**: Uses `Selenium` for dynamic JavaScript-rendered pages (if needed).
- **NLP & Content Filtering**: Uses `Spacy`, `KeyBERT`, and other NLP tools to extract relevant content based on user instructions.
- **Keyword Extraction**: Utilizes `KeyBERT` to automatically extract keywords from user instructions.
- **Similarity Scoring**: Implements sentence similarity using a pre-trained `sentence-transformers` model.
- **Export to JSON**: Scraped data is saved in a structured JSON format for downstream processing.

## Project Structure

```bash
Rufus/
│
├── src/
│   ├── client.py                # RufusClient class for handling scraping logic
│   ├── web_scraper.py               # Core web scraping and link crawling logic
│   ├── nlp_web.py                   # NLP and content filtering logic
│   ├── utils.py                 # Utility functions (resilient requests, save to JSON, etc.)
├── test.py                           # Unit tests for the scraping functions
├── requirements.txt             # List of project dependencies
├── README.md                    # Project documentation (this file)
└── main.py                      # Entry point for running the RufusClient

```

## How to Use
### Prerequisites
- Python 3.11 or later
- A virtual environment or conda environment set up
- Required dependencies (listed in requirements.txt)

### Installation
-  Clone the Repository:
     ```bash
     git clone https://github.com/dhirdhir1997/Rufus
     cd Rufus
     ```
- Create and Activate a Virtual Environment:
  ```bash
  conda create --name rufus-env python=3.11
  conda activate rufus-env
  ```
- Install Dependencies:
    ```bash
    pip install -r requirements.txt
     ```
### Running the application
- Run the Scraper:
    To scrape information from North Carolina State University (NCSU), run the following command:
     ```bash
    python main.py
     ```
- Modify Instructions:
    If you want to scrape for different information, modify the instructions variable in main.py.
    ```bash
    instructions = "Give me all information about North Carolina State University"
    ```
- Check Results:
    After running the scraper, the data will be saved as output.json. Open it to see the structured results:
     ```bash
    {
    "timestamp": "2024-10-22 14:35:00",
    "results": [
        {
            "url": "https://www.ncsu.edu/link1",
            "content": ["Information about NCSU from the link"]
        },
        {
            "url": "https://www.ncsu.edu/link2",
            "content": ["More information about NCSU"]
        }
    ]
}
    
 ```
    

  
  

     

     

  






