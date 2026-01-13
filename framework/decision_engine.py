# framework/decision_engine.py

class DecisionEngine:
    """
    A rule-based decision engine for an agent.
    
    This engine uses simple if/elif/else logic to decide on an action
    based on the agent's current perception.
    """

    def __init__(self, rules=None):
        """
        Initializes the DecisionEngine.

        Args:
            rules (dict, optional): A dictionary of rules where keys are 
                conditions and values are actions. For now, we'll hardcode them.
        """
        # In a more advanced version, you could pass rules in.
        # For now, we'll define them directly in the make_decision method.
        print("DecisionEngine initialized.")

    def make_decision(self, perception: dict, memory: dict, capabilities: list):
        """
        Makes a decision based on a set of rules.

        Args:
            perception (dict): The current perception from the environment.
            memory (dict): The agent's memory.
            capabilities (list): The list of actions the agent is capable of.

        Returns:
            str: The chosen action.
        """
        print("DecisionEngine is analyzing perception...")
        
        # Get the user's input from the perception dictionary
        user_input = perception.get("user_input", "").lower() # Use .lower() to make matching easier

        # Rule 1: Check for a greeting
        if "hello" in user_input or "hi" in user_input:
            if "greeting" in capabilities:
                return "greeting"

        # Rule 2: Check for a question
        if "?" in user_input:
            if "answer_question" in capabilities:
                return "answer_question"

        # Rule 3: Default action if no other rules match
        return "no_action"