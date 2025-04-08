import requests
from bs4 import BeautifulSoup
from crewai.tools import Tool
from typing import Optional

class WebScraperTool(Tool):
    """Tool to scrape content from websites."""
    
    name: str = "Web Scraper"
    description: str = (
        "Scrapes content from websites and extracts text from paragraphs. "
        "Useful for gathering information from web pages for research or content creation."
    )

    def _run(self, url: str) -> str:
        """Scrapes content from the given URL."""
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                paragraphs = soup.find_all('p')
                return "\n".join(p.get_text() for p in paragraphs[:5])
            return f"Failed to fetch {url}: HTTP {response.status_code}"
        except Exception as e:
            return f"Error while scraping {url}: {str(e)}" 