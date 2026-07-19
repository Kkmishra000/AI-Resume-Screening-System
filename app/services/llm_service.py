import os

from dotenv import load_dotenv
from pathlib import Path
import google.generativeai as genai

env_path = Path(__file__).resolve().parent.parent / ".env"  # Adjust the path to your .env file
load_dotenv(dotenv_path=env_path)  # Load environment variables from .env file

api_key = os.getenv("GEMINI_API_KEY")# Get the Gemini API key from environment variables

genai.configure(api_key=api_key)  # Configure the Gemini API with the API key



model = genai.GenerativeModel("gemini-3.5-flash")  # Load the Gemini 3.5 Flash model

def generate_answer(context,question):
    
    context_text = "\n".join(context)  # Join the context chunks into a single string
    
    prompt = f"""
You are an AI Resume Screening Assistant.

Context:
{context_text}

Question:
{question}

Instructions:
- Answer only using the provided context.
- Do not make assumptions.
- If the answer is not present in the context, reply:
"The resume does not contain this information."

Answer:
"""
    
    response = model.generate_content(prompt)
   
    return response.text