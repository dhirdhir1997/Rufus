import unittest
from unittest.mock import patch, MagicMock
from src.scraper import scrape_website
from datetime import datetime

class TestScrapeWebsite(unittest.TestCase):
    
    @patch('src.scraper.simple_crawl')
    def test_valid_url_and_instructions(self, mock_simple_crawl):
        url = "https://www.ncsu.edu"
        instructions = "Test instructions"
        mock_simple_crawl.return_value = MagicMock()

        result = scrape_website(url, instructions)
        self.assertIsNotNone(result)

    @patch('src.scraper.simple_crawl')
    def test_invalid_url(self, mock_simple_crawl):
        url = "invalid_url"
        instructions = "Test instructions"
        mock_simple_crawl.return_value = None

        result = scrape_website(url, instructions)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
