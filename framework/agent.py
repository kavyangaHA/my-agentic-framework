class Agent:
    def __init__(self,name:str,capabilities:list = None):

        self.name = name
        self.capabilities = capabilities if capabilities is not None else []
        self.memory ={}
        self.environment = None #will be set when the agent is added to an environment

    def perceive(self):

        print(f"[{self.name}] is perceiving the environment.")
        if not self.environment:
            print(f"[{self.name}] has no environment to perceive.")
            return {}
        perception = self.environment.get_state_for_agent(self.name)
        print(f"[{self.name}] perceived: {perception}")
        return perception
    
    def decide(self,perception:dict):

        print(f"[{self.name}] is deciding...")
        decision = "No_action_yet"
        print(f"[{self.name}] decided to: {decision}")
        return decision
    
    def act(self,decision:str):
        print(f"[{self.name}] is acting...")
        print(f"[{self.name}] performed action: {decision}(placeholder)")

    def run_cycle(self):
        print(f"\n-- starting cycle for [{self.name}] --")
        perception = self.perceive()
        decision = self.decide(perception)
        self.act(decision)
        print(f"--cycle for [{self.name}] finished --\n")

