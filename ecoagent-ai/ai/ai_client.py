import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

class AIClient:
    """
    Wrapper for Gemini and Ollama (Granite).
    Prioritizes Gemini if GOOGLE_API_KEY is present.
    """
    
    def __init__(self):
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.ollama_model = os.getenv("OLLAMA_MODEL", "granite-code:8b")
        
        self.mode = "google" if self.google_api_key else "ollama"
        self.engine = self._initialize_engine()

    def _initialize_engine(self):
        if self.mode == "google":
            return ChatGoogleGenerativeAI(
                model="gemini-3.5-flash",
                google_api_key=self.google_api_key,
                temperature=0.7
            )
        else:
            return Ollama(
                base_url=self.ollama_base_url,
                model=self.ollama_model
            )

    def get_response(self, prompt, system_prompt="You are a sustainability expert."):
        if self.mode == "google":
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=prompt)
            ]
            response = self.engine.invoke(messages)
            return response.content
        else:
            # Ollama format
            full_prompt = f"System: {system_prompt}\n\nUser: {prompt}\n\nAssistant:"
            return self.engine.invoke(full_prompt)

    def is_available(self):
        # Basic check
        if self.mode == "google" and self.google_api_key:
            return True
        # For Ollama, would need a health check, but we'll assume true if configured
        return True
