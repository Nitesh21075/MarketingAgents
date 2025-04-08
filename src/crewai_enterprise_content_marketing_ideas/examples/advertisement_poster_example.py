import os
import sys

# Add the parent directory to the path so we can import the tool
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crewai_enterprise_content_marketing_ideas.tools.advertisement_poster_tool import AdvertisementPosterTool

def main():
    """
    Example script demonstrating how to use the AdvertisementPosterTool directly.
    """
    print("Advertisement Poster Generator Example")
    print("=====================================")
    
    # Create an instance of the AdvertisementPosterTool
    poster_generator = AdvertisementPosterTool()
    
    # Run the tool to generate a poster
    result = poster_generator.run("Generate an advertisement poster")
    
    # Print the result
    print("\nResult:")
    print(result)

if __name__ == "__main__":
    main() 