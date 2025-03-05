import requests
import json
from typing import Optional, Dict, Any

class GeminiRealtimeAPI:
    def __init__(self, api_key: str):
        """
        Initialize the Gemini Realtime API client.
        """
        self.api_key = "AIzaSyBuPMBvEB93Ce8NJu6trFXJH2VEkMrXMdk"
        self.base_url = "https://generativelanguage.googleapis.com/v1alpha/models/gemini-2.0-flash-exp:generateContent"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def analyze(self, user_input: str) -> str:
        """
        Analyze user input and plan the steps to complete the task. then invoke the agents and give them the plan and the steps to perform.
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
                self.base_url,
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
        Generate a response for the user query. make sure to keep the contxt in mind.
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
                self.base_url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            result = response.json()
            return result.get("candidates", [])[0].get("content", {}).get("parts", [])[0].get("text", "")
        except Exception as e:
            print(f"Error generating response: {e}")
            return ""