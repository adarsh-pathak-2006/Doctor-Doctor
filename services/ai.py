from google import genai
from django.conf import settings

client=genai.Client(api_key=settings.GEMINI_API_KEY)

def generate_response(defined_prompt):
    response=client.models.generate_content(
        model='gemini-2.5-flash',
        contents=defined_prompt
    )
    return response.text.strip()

