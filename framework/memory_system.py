# framework/memory_system.py

class MemorySystem:
    """
    A simple memory system for an agent.
    
    For now, it's a wrapper around a dictionary, but it allows for
    future expansion (e.g., search, memory limits, etc.).
    """

    def __init__(self):
        """Initializes the MemorySystem."""
        self.memory = {}
        print("MemorySystem initialized.")

    def store(self, key: str, value):
        """Stores a key-value pair in memory."""
        self.memory[key] = value
        print(f"Memory: Stored '{key}'.")

    def retrieve(self, key: str):
        """Retrieves a value from memory by its key."""
        return self.memory.get(key)

    def get_all(self):
        """Returns the entire memory dictionary."""
        return self.memory