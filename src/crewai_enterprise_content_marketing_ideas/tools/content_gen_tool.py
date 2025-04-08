from crewai.tools import Tool
from typing import Optional

class ContentGeneratorTool(Tool):
    """Tool to generate various types of content."""
    
    name: str = "Content Generator"
    description: str = (
        "Generates different types of content based on the prompt. "
        "Can create posters, captions, video ideas, and other creative assets."
    )

    def _run(self, prompt: str) -> str:
        """Generates content based on the given prompt."""
        if "poster" in prompt.lower():
            return "Generated poster image URL: https://example.com/poster123.png"
        elif "caption" in prompt.lower():
            return "Generated caption: 'Unleash your style. #FashionRevolution'"
        elif "video" in prompt.lower():
            return "Generated video URL: https://example.com/video_reel.mp4"
        return "Generated generic creative asset." 