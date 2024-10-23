from .scraper import scrape_website

class RufusClient:
    """
    A client class that interfaces with the Rufus scraping system.
    """
    
    def scrape(self, url, instructions):
        """
        Scrape the given URL for information based on the provided instructions.
        
        Args:
            url (str): The URL to scrape.
            instructions (str): Instructions for what content to scrape.
        
        Returns:
            dict: A dictionary of scraped content and associated metadata.
        """
        if not url or not instructions:
            raise ValueError("URL and instructions are required.")

        try:
            # Call the scrape_website function to perform the scraping.
            return scrape_website(url, instructions)
        except Exception as e:
            print(f"Error while scraping: {e}")
            return None
