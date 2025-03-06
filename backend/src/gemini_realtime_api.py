import requests
# import json
# from typing import Optional, Dict, Any

class GeminiRealtimeAPI:
    def __init__(self):
        """
        Initialize the Gemini Realtime API client.
        """
        self.api_key = "AIzaSyBuPMBvEB93Ce8NJu6trFXJH2VEkMrXMdk"
        self.base_url = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro-vision:generateContent"
        self.headers = {
            "Content-Type": "application/json",
        }

    def analyze(self, user_input: str) -> str:
        """
        Analyze user input and plan the steps to complete the task. then invoke the agents and give them the plan and the steps to perform. 
        The agents are an assistant agent that looks at the user camera or screen to guide the user, a coder agent that grenerates code and has an environment, and a computer agent that can perform CRUD operatio
        in user's files, and can run commands in the user's machine.
        """
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {"text": user_input}
                    ]
                }
            ]
        }
        try:
            response = requests.post(
                f"{self.base_url}?key={self.api_key}",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            result = response.json()
            return result.get("candidates", [])[0].get("content", {}).get("parts", [])[0].get("text", "")
        except Exception as e:
            print(f"Error analyzing input: {e}")
            return ""

    def generate_response(self, user_input: str) -> str:
        """
        Generate a response for the user query. make sure to keep the contxt and intent in mind.
        """
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {"text": user_input}
                    ]
                }
            ]
        }
        try:
            response = requests.post(
                f"{self.base_url}?key={self.api_key}",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            result = response.json()
            return result.get("candidates", [])[0].get("content", {}).get("parts", [])[0].get("text", "")
        except Exception as e:
            print(f"Error generating response: {e}")
            return ""