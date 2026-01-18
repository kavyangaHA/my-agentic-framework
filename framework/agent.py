from .decision_engine import DecisionEngine
from .action_module import ActionModule
from .memory_system import MemorySystem


class Agent:
    def __init__(self,name:str,capabilities:list = None):
        self.name = name
        self.capabilities = capabilities if capabilities is not None else []
        self.memory ={}
        self.environment = None #will be set when the agent is added to an environment
        #mulinm agent wwa create krpu gmn eyw environment ekakat add krn kl eyge environment ek None
        
        #initialize the brain,hands and memory
        self.decision_engine = DecisionEngine() # to give the agent a brain
        self.action_module = ActionModule()   # to give the agent hands
        self.memory_system = MemorySystem()   # to give the agent memory
    
    def perceive(self):

        print(f"[{self.name}] is perceiving the environment.")
        if not self.environment:
            print(f"[{self.name}] has no environment to perceive.")
            return {}
        perception = self.environment.get_state_for_agent(self.name)#environment cls ekedi agentwai environment ekai link krl thiyenne
        print(f"[{self.name}] perceived: {perception}")
        return perception
    
    def decide(self,perception:dict):

        print(f"[{self.name}] is deciding...")
        decision = self.decision_engine.make_decision(perception, self.memory, self.capabilities)
        print(f"[{self.name}] decided to: {decision}")
        return decision
    
    def act(self,decision:str):
        print(f"[{self.name}] is acting...")
        #print(f"[{self.name}] performed action: {decision}(placeholder)")
        result = self.action_module.execute(decision, context={"agent": self})
        print(f"[{self.name}] Action result: {result}")
        return result
    
    def run_cycle(self):
        print(f"\n-- starting cycle for [{self.name}] --")
        perception = self.perceive()
        decision = self.decide(perception)
        #self.act(decision)
        action_result = self.act(decision)
        #store the result of the cycle in memory
        self.memory_system.store("last_action_result", action_result)
        print(f"--cycle for [{self.name}] finished --\n")
