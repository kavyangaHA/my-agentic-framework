# framework/decision_engine.py (CORRECTED for the new google-genai library)

from google import genai
import os
from dotenv import load_dotenv
import json

class DecisionEngine:
    """
    A Google Gemini-based decision engine using the new 'google-genai' library.
    """

    def __init__(self, model_name='gemini-3-flash-preview'):
        """
        Initializes the DecisionEngine by creating a configured client.
        """
        # Load environment variables from .env file
        load_dotenv()
        
        # Get the API key from environment variables
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env file or environment variables.")
        
        # Create a configured client with the API key
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name
        print(f"Gemini DecisionEngine initialized with model: {model_name}")

    def make_decision(self, perception: dict, memory: dict, capabilities: list):
        """
        Makes a decision by querying the Gemini API using the client.
        """
        print("Gemini DecisionEngine is thinking...")
        
        # 1. Craft the prompt for the LLM
        full_prompt = self._create_full_prompt(perception, memory, capabilities)

        try:
            # 2. Make the API call using the client object
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=full_prompt
            )
            
            # 3. Parse the response
            decision_data = json.loads(response.text)
            chosen_action = decision_data.get("action")

            if chosen_action in capabilities:
                print(f"Gemini decided to: {chosen_action}")
                return chosen_action
            else:
                print(f"Gemini chose an invalid action '{chosen_action}'. Defaulting to 'no_action'.")
                return "no_action"

        except json.JSONDecodeError:
            print(f"Gemini response was not valid JSON: {response.text}. Defaulting to 'no_action'.")
            return "no_action"
        except Exception as e:
            print(f"An error occurred during Gemini decision making: {e}")
            return "no_action"

    def _create_full_prompt(self, perception: dict, memory: dict, capabilities: list) -> str:
        """Creates the full prompt for the Gemini model."""
        capabilities_str = ", ".join(capabilities)
        return f"""
        You are a decision-making module for an AI agent.
        Your only task is to choose the best action from a list of available capabilities.
        You must respond with a JSON object containing a single key "action".
        The value for "action" must be one of the following: {capabilities_str}.
        If no capability is suitable, choose "no_action".
        Do not add any explanations or text outside of the JSON object.

        Here is the current situation:
        - Perception: {perception}
        - Memory: {memory}
        
        Based on this, choose the best action and respond with only the JSON object.
        """