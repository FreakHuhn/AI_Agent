import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

try:
    models = client.models.list()
    print("Verfügbare Modelle:")
    for model in models:
        print(f"- {model.name}")
except Exception as e:
    print(f"Fehler beim Abrufen der Modelle: {e}")
