# framework/communication_hub.py

class CommunicationHub:
    """
    A central hub for passing messages between agents in an environment.
    """

    def __init__(self):
        """Initializes the CommunicationHub."""
        self.message_queue = []  # A list to hold messages
        self.subscribers = {}    # A dictionary to hold who is listening for what
        print("CommunicationHub initialized.")

    def subscribe(self, agent, message_types=None):
        """
        Allows an agent to subscribe to receive messages.

        Args:
            agent (Agent): The agent object that is subscribing.
            message_types (list, optional): A list of message types the agent 
                is interested in. If None, subscribes to all messages.
        """
        for msg_type in message_types or ["all"]:
            if msg_type not in self.subscribers:
                self.subscribers[msg_type] = []
            if agent not in self.subscribers[msg_type]:
                self.subscribers[msg_type].append(agent)
        print(f"Agent '{agent.name}' subscribed to messages: {message_types or 'all'}")

    def broadcast(self, message, sender, message_type="general"):
        """
        Sends a message to all subscribed agents.

        Args:
            message (str): The content of the message.
            sender (Agent): The agent sending the message.
            message_type (str, optional): The type of message. Defaults to "general".
        """
        print(f"\n[COMM] Agent '{sender.name}' broadcasting a '{message_type}' message: '{message}'")
        full_message = {
            "content": message,
            "sender": sender.name,
            "type": message_type
        }
        self.message_queue.append(full_message)
        self._deliver_message(full_message)

    def _deliver_message(self, full_message):
        """Delivers a message to all relevant subscribers."""
        message_type = full_message["type"]
        # Find all agents who should receive this message
        recipients = self.subscribers.get("all", []) + self.subscribers.get(message_type, [])
        
        # Remove duplicates from the recipient list
        unique_recipients = list(set(recipients))

        for agent in unique_recipients:
            # Don't send the message back to the sender
            if agent.name != full_message["sender"]:
                agent.receive_message(full_message)