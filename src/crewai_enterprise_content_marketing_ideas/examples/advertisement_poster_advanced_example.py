import os
import sys

# Add the parent directory to the path so we can import the tool
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crewai_enterprise_content_marketing_ideas.tools.advertisement_poster_tool import AdvertisementPosterTool, PosterDetails

def main():
    """
    Advanced example script demonstrating how to use the AdvertisementPosterTool
    with more specific parameters.
    """
    print("Advanced Advertisement Poster Generator Example")
    print("=============================================")
    
    # Create an instance of the AdvertisementPosterTool
    poster_generator = AdvertisementPosterTool()
    
    # Example 1: Generate a poster with specific details
    print("\nExample 1: Generate a poster with specific details")
    print("-------------------------------------------------")
    
    # Create a PosterDetails object with specific information
    details = PosterDetails(
        product_name="Eco-Friendly Water Bottle",
        target_audience="Environmentally conscious consumers aged 25-45",
        key_features=["100% recyclable materials", "Keeps drinks cold for 24 hours", "BPA-free"],
        call_to_action="Join the eco-revolution today!",
        brand_voice="Modern, eco-conscious, and premium"
    )
    
    # Convert the details to a string
    details_str = f"""
    Product: {details.product_name}
    Target Audience: {details.target_audience}
    Key Features: {', '.join(details.key_features)}
    Call to Action: {details.call_to_action}
    Brand Voice: {details.brand_voice}
    """
    
    # Run the tool with the specific details
    result1 = poster_generator.run(details_str)
    
    # Print the result
    print("\nResult:")
    print(result1)
    
    # Example 2: Generate a poster with a different prompt
    print("\nExample 2: Generate a poster with a different prompt")
    print("-------------------------------------------------")
    
    # Run the tool with a different prompt
    result2 = poster_generator.run("Create a poster for a new smartphone with advanced AI features")
    
    # Print the result
    print("\nResult:")
    print(result2)

if __name__ == "__main__":
    main() 