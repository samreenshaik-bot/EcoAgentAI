import os
from dotenv import load_dotenv
from ai.ai_client import AIClient

def test_connection():
    print("🚀 Initializing Gemini Connection Test...")
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        print("❌ ERROR: GOOGLE_API_KEY is not set in .env")
        print("Please visit https://aistudio.google.com/ to get your key.")
        return

    try:
        client = AIClient()
        print(f"📡 Mode: {client.mode.upper()}")
        if client.mode == "google":
             print(f"🤖 Model: {client.engine.model}")
        
        test_prompt = "Hello! Briefly explain why sustainability is important for AI projects."
        print(f"📝 Test Prompt: {test_prompt}")
        
        response = client.get_response(test_prompt)
        
        print("\n✅ Response Received:")
        print("-" * 50)
        print(response)
        print("-" * 50)
        print("\n✨ Connection Successful!")
        
    except Exception as e:
        print(f"❌ FAILED: {str(e)}")

if __name__ == "__main__":
    test_connection()
