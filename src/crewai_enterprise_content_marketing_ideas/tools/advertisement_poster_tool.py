import os
import google.generativeai as genai
from crewai.tools import tool
from pydantic import BaseModel, Field
from typing import Optional
from PIL import Image
import io

# Configure Gemini API
GEMINI_API_KEY = ""
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')

class PosterDetails(BaseModel):
    """Details for generating an advertisement poster."""
    product_name: str = Field(..., description="Name of the product being advertised (e.g., 'SuperStride Shoes')")
    target_audience: str = Field(..., description="The intended audience for the poster (e.g., 'Young athletes', 'Fashion-conscious adults')")
    key_message: str = Field(..., description="The main message or benefit to highlight (e.g., 'Unleash your speed!', 'Comfort and style combined')")
    call_to_action: Optional[str] = Field(None, description="What you want people to do (e.g., 'Shop now!', 'Visit our website', 'Find a store near you')")
    brand_name: Optional[str] = Field(None, description="The name of the brand")
    slogan: Optional[str] = Field(None, description="A catchy slogan for the product or brand")
    visual_style: Optional[str] = Field(None, description="Desired visual style (e.g., 'Modern and minimalist', 'Bold and energetic', 'Elegant and classic')")
    color_palette: Optional[str] = Field(None, description="Desired color scheme (e.g., 'Blue and white', 'Bright and vibrant', 'Neutral tones')")
    include_logo: bool = Field(False, description="Whether to include the brand logo")
    logo_prompt_part: Optional[str] = Field(None, description="A description of the brand logo to include in the image prompt if include_logo is True")
    additional_notes: Optional[str] = Field(None, description="Any other specific instructions or details for the image")

class AdvertisementPosterTool(tool):
    """Tool to generate advertisement posters using the Gemini API."""
    
    name: str = "Advertisement Poster Generator"
    description: str = (
        "Collects details for an advertisement poster and generates an image using the Gemini API, "
        "saving it as a PNG file. This tool is useful for creating marketing materials for products."
    )

    def _ask_for_poster_details(self) -> PosterDetails:
        """Asks the user for details about the advertisement poster."""
        print("\nLet's gather some information for your advertisement poster:")

        product_name = input("What is the name of the product you are advertising? ")
        target_audience = input("Who is the target audience for this poster? ")
        key_message = input("What is the key message or benefit you want to highlight? ")
        call_to_action = input("What call to action do you want to include (e.g., 'Shop now!', leave blank if none)? ") or None
        brand_name = input("What is the name of the brand (leave blank if none)? ") or None
        slogan = input("Do you have a slogan for the product or brand (leave blank if none)? ") or None
        visual_style = input("What kind of visual style do you envision (e.g., 'Modern', 'Bold', leave blank for default)? ") or None
        color_palette = input("Do you have a specific color palette in mind (e.g., 'Blue and white', leave blank for default)? ") or None

        include_logo_input = input("Do you want to include a brand logo in the image? (yes/no): ").lower()
        include_logo = include_logo_input == 'yes'
        logo_prompt_part = None
        if include_logo:
            logo_prompt_part = input("Please describe your brand logo so I can include it in the image: ")

        additional_notes = input("Do you have any other specific instructions or details for the image? ") or None

        return PosterDetails(
            product_name=product_name,
            target_audience=target_audience,
            key_message=key_message,
            call_to_action=call_to_action,
            brand_name=brand_name,
            slogan=slogan,
            visual_style=visual_style,
            color_palette=color_palette,
            include_logo=include_logo,
            logo_prompt_part=logo_prompt_part,
            additional_notes=additional_notes
        )

    def _run(self, argument: str = "start") -> str:
        """Generates an advertisement poster image using Gemini based on user input."""
        poster_details = self._ask_for_poster_details()

        prompt = f"Create an advertisement poster for {poster_details.product_name} targeting {poster_details.target_audience}. "
        prompt += f"The key message should be: '{poster_details.key_message}'. "
        if poster_details.call_to_action:
            prompt += f"Include the call to action: '{poster_details.call_to_action}'. "
        if poster_details.brand_name:
            prompt += f"The brand name is {poster_details.brand_name}. "
        if poster_details.slogan:
            prompt += f"Include the slogan: '{poster_details.slogan}'. "
        if poster_details.visual_style:
            prompt += f"The visual style should be {poster_details.visual_style}. "
        if poster_details.color_palette:
            prompt += f"Use a color palette of {poster_details.color_palette}. "
        if poster_details.include_logo and poster_details.logo_prompt_part:
            prompt += f"Include a representation of the brand logo: {poster_details.logo_prompt_part}. "
        if poster_details.additional_notes:
            prompt += f"Additional notes: {poster_details.additional_notes}. "
        prompt += "The poster should be visually appealing and effective for advertising."

        try:
            response = model.generate_content([prompt])
            response.raise_for_status()
            image_data = response.parts[0].data['mime_type'], response.parts[0].data['data']

            if image_data and image_data[0] == 'image/png':
                image = Image.open(io.BytesIO(image_data[1]))
                filename = f"{poster_details.product_name.replace(' ', '_').lower()}_advertisement.png"
                image.save(filename)
                return f"Advertisement poster generated and saved as '{filename}'."
            else:
                return "Error: Received non-PNG image data from Gemini."

        except Exception as e:
            return f"Error generating poster: {e}"


if __name__ == '__main__':
    # Example of how to use the tool
    poster_generator_tool = AdvertisementPosterTool()
    result = poster_generator_tool.run("Generate an advertisement poster")
    print(result) 
