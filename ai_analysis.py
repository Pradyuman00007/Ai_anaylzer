import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-pro")

async def analyze_with_gemini(sector: str, raw_data: str) -> str:
    prompt = f"""Analyze the following market data for the {sector} sector in India and highlight trade opportunities:
    
    {raw_data}
    
    Format the response as a structured markdown report with headers like:
    ## Sector Overview
    ## Current Trends
    ## Trade Opportunities
    ## Risks and Considerations
    """

    response = model.generate_content(prompt)
    return response.text
