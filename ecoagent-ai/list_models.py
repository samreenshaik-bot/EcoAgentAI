import os
import google.generativeai as genai
from dotenv import load_dotenv

def list_supported_models():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("❌ Error: GOOGLE_API_KEY not found.")
        return

    genai.configure(api_key=api_key)
    
    print("🔍 Fetching available models for your API key...\n")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ Model found: {m.name}")
    except Exception as e:
        print(f"❌ Failed to list models: {str(e)}")

if __name__ == "__main__":
    list_supported_models()
