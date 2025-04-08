# CrewAI Enterprise Content Marketing Ideas

This project uses CrewAI to generate content marketing ideas and advertisement posters.

## Advertisement Poster Generator Tool

The `AdvertisementPosterTool` is a custom tool that uses the Gemini API to generate advertisement posters based on user input. It collects information about the product, target audience, key message, and other design elements, then uses Gemini to create a visually appealing poster image.

### Prerequisites

- Python 3.8+
- Gemini API key

### Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install crewai google-generativeai pillow
```

3. Set your Gemini API key as an environment variable:

```bash
# Windows (PowerShell)
$env:GEMINI_API_KEY = 'your_api_key_here'

# Windows (CMD)
set GEMINI_API_KEY=your_api_key_here

# Linux/macOS
export GEMINI_API_KEY='your_api_key_here'
```

### Usage

#### As a standalone tool

You can use the `AdvertisementPosterTool` directly by running the example script:

```bash
python src/crewai_enterprise_content_marketing_ideas/examples/generate_poster_example.py
```

This will prompt you for information about the advertisement poster and then generate an image using the Gemini API.

#### As part of the CrewAI workflow

The tool is also integrated into the CrewAI workflow. To use it as part of the workflow:

1. Make sure your Gemini API key is set as an environment variable
2. Run the main script:

```bash
python src/crewai_enterprise_content_marketing_ideas/main.py
```

The `marketing_designer` agent will use the `AdvertisementPosterTool` to generate an advertisement poster based on the topic and company provided.

### Customization

You can customize the `AdvertisementPosterTool` by modifying the `src/crewai_enterprise_content_marketing_ideas/tools/advertisement_poster_tool.py` file. The tool uses the Gemini API to generate images, so you can adjust the prompt to get different styles of posters.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
