# from .gemini_realtime_api import GeminiRealtimeAPI  # Hypothetical Gemini API client

# class LLMService:
#     def __init__(self):
#         self.gemini = GeminiRealtimeAPI()  # Initialize Gemini API client

#     async def generate_response(self, user_input: str) -> str:
#         """
#         Generate a response using the Gemini API.
#         """
#         try:
#             # Use Gemini API to generate a response
#             response = await self.gemini.generate_response(user_input)
#             return response
#         except Exception as e:
#             raise Exception(f"Error generating LLM response: {str(e)}")
        
from google import genai

class LLMService:
    def __init__(self):
        # Configure API key
        genai.configure(api_key="AIzaSyBuPMBvEB93Ce8NJu6trFXJH2VEkMrXMdk")
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    async def generate_response(self, user_input: str) -> str:
        """
        Generate a response using the Google Gemini API.
        """
        try:
            # Generate response using Google's Gemini model
            response = self.model.generate_content(user_input)
            return response.text if response else "No response received."
        except Exception as e:
            raise Exception(f"Error generating LLM response: {str(e)}")
