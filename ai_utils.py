import os
from groq import Groq
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("⚠️ Missing GROQ_API_KEY in .env file")

# Initialize Groq client
client = Groq(api_key=api_key)

def generate_summary(text: str) -> str:
    """Generate a summary for the given text"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ latest stable Groq model
        messages=[{"role": "user", "content": f"Summarize this:\n\n{text}"}],
    )
    return response.choices[0].message.content

def generate_questions(text: str) -> str:
    """Generate questions from the given text"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": f"Create 5 questions from:\n\n{text}"}],
    )
    return response.choices[0].message.content

def chat_with_ai(prompt: str) -> str:
    """General chat with AI"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
