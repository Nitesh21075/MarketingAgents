#!/usr/bin/env python
"""
Example script demonstrating how to use the AdvertisementPosterTool directly.
"""
import os
import sys
from pathlib import Path

# Add the parent directory to the path so we can import the tool
sys.path.append(str(Path(__file__).parent.parent.parent))

from crewai_enterprise_content_marketing_ideas.tools.advertisement_poster_tool import AdvertisementPosterTool

def main():
    """
    Run the advertisement poster generation tool.
    """
    # Check if the GEMINI_API_KEY environment variable is set
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please set it using one of the following commands:")
        print("  - Windows (PowerShell): $env:GEMINI_API_KEY = 'your_api_key_here'")
        print("  - Windows (CMD): set GEMINI_API_KEY=your_api_key_here")
        print("  - Linux/macOS: export GEMINI_API_KEY='your_api_key_here'")
        return

    # Create an instance of the AdvertisementPosterTool
    poster_tool = AdvertisementPosterTool()
    
    # Run the tool
    result = poster_tool.run("Generate an advertisement poster")
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main() 