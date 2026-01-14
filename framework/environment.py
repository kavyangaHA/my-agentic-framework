class Environment:
    def __init__(self, name:str = "Default_Environment"):
        self.name = name
        self.state = {} #A dictionary to hold the environment state
        self.agents = [] #A list to hold all agents in the environment


    def add_agent(self, agent):
        if agent not in self.agents:
            self.agents.append(agent)
            agent.environment = self #Set the agent's environment to this environment(linking agent to environment)
            print(f"Agent [{agent.name}] added to environment [{self.name}].")
        else:
            print(f"Agent [{agent.name}] is already in environment [{self.name}].") 

    def get_state_for_agent(self, agent_name:str):
        print(f"Getting state for agent [{agent_name}].")
        return self.state      

    def update_state(self, key:str, value):
        self.state[key] = value
        print(f"Environment state updated: {key} = {value}") 