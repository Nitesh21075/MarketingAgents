#!/usr/bin/env python
"""
Example script demonstrating how to use the WebScraperTool directly.
"""
import os
import sys
from pathlib import Path

# Add the parent directory to the path so we can import the tool
sys.path.append(str(Path(__file__).parent.parent.parent))

from crewai_enterprise_content_marketing_ideas.tools.web_scraper import WebScraperTool

def main():
    """
    Run the web scraper tool.
    """
    # Create an instance of the WebScraperTool
    scraper_tool = WebScraperTool()
    
    # Get the URL from command line arguments or use a default
    url = sys.argv[1] if len(sys.argv) > 1 else "https://www.example.com"
    
    # Run the tool
    result = scraper_tool.run(url)
    
    # Print the result
    print("\nScraped Content:")
    print("-" * 50)
    print(result)
    print("-" * 50)

if __name__ == "__main__":
    main() 