# framework/action_module.py

class ActionModule:
    """
    Handles the execution of actions for an agent.
    
    This module maps action names (like "greeting") to actual methods
    that produce a result.
    """

    def __init__(self):
        """Initializes the ActionModule and defines available actions."""
        self.actions = {
            "greeting": self._greeting,
            "answer_question": self._answer_question,
            "clarify":self._clarify,
            "no_action": self._no_action,

        }
        print("ActionModule initialized.")

    def execute(self, action_name: str, context: dict = None):
        """
        Executes the specified action.

        Args:
            action_name (str): The name of the action to execute.
            context (dict, optional): Information about the agent or environment.

        Returns:
            str: The result of the action.
        """
        print(f"ActionModule is executing '{action_name}'...")
        
        action = self.actions.get(action_name)
        
        if action:
            return action(context)
        else:
            return f"Error: Action '{action_name}' not found."

    # --- Private action methods ---
    
    def _greeting(self, context: dict = None):
        """Returns a friendly greeting."""
        agent_name = context.get("agent", {}).name if context and context.get("agent") else "Agent"
        return f"Hello! My name is {agent_name}. How can I help you today?"

    def _answer_question(self, context: dict = None):
        """Returns a placeholder answer for a question."""
        return "That's a great question! I am still learning how to answer specific questions."

    def _clarify(self,context:dict = None):
        return "I'm not sure I understand. Could you please clarify it?"
    
    def _no_action(self, context: dict = None):
        """Handles cases where no specific action is chosen."""
        return "I am not sure how to respond to that."