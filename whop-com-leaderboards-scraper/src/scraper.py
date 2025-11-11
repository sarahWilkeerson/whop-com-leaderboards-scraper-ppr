thonimport requests
import json
import time
import logging
from .extractors.whop_parser import parse_leaderboard
from .extractors.utils import get_proxy, save_data

logging.basicConfig(level=logging.INFO)

def scrape_leaderboard(url, proxy=None):
    try:
        logging.info(f"Scraping URL: {url}")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        response = requests.get(url, headers=headers, proxies=proxy)
        response.raise_for_status()
        data = parse_leaderboard(response.text)
        save_data(data, "output.json")
        logging.info(f"Data successfully saved.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during scraping: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def main():
    start_urls = ["https://whop.com/discover/leaderboards/", "https://whop.com/discover/leaderboards/f/most_reviews_24_hours/"]
    for url in start_urls:
        proxy = get_proxy()
        scrape_leaderboard(url, proxy)
        time.sleep(2)  # To avoid rate-limiting

if __name__ == "__main__":
    main()