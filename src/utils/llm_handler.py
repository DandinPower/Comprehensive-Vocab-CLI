from abc import ABC, abstractmethod
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class LLMHandler(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def invoke(self, prompt:str) -> str:
        pass

class GeminiProHandler(LLMHandler):
    def __init__(self):
        super().__init__()
        self.chat_llm = ChatGoogleGenerativeAI(model = "gemini-pro", google_api_key = GOOGLE_API_KEY)

    def invoke(self, prompt:str) -> str:
        result = self.chat_llm.invoke(prompt)
        return result.content
    
class GPT4oMiniHandler(LLMHandler):
    def __init__(self):
        super().__init__()
        self.chat_llm = ChatOpenAI(model = "gpt-4o-mini", api_key = OPENAI_API_KEY)

    def invoke(self, prompt:str) -> str:
        result = self.chat_llm.invoke(prompt)
        return result.content