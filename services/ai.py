import json
from google import genai
from django.conf import settings

client=genai.Client(api_key=settings.GEMINI_API_KEY)

def generate_response(defined_prompt):
    response=client.models.generate_content(
        model='gemini-2.5-flash',
        contents=defined_prompt
    )
    raw_text = response.text.strip()
    
    # Strip out potential markdown code blocks if the model outputs them
    if raw_text.startswith("```json"):
        raw_text = raw_text[7:]
    elif raw_text.startswith("```"):
        raw_text = raw_text[3:]
    if raw_text.endswith("```"):
        raw_text = raw_text[:-3]
        
    raw_text = raw_text.strip()
    
    try:
        data = json.loads(raw_text)
        return data
    except json.JSONDecodeError:
        # Fallback in case the model does not strictly return JSON
        return {
            "prescription": "Error: Could not parse prescription.",
            "condition_analysis": raw_text
        }

