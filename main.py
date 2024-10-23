from src.client import RufusClient

if __name__ == "__main__":
    client = RufusClient()

    # Updated URL and instructions for NC State University
    instructions = "Give me all information about North Carolina State University"
    documents = client.scrape("https://www.ncsu.edu", instructions)
    print(documents)
