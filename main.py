#print("Hello, World!")

from framework.agent import Agent
from framework.environment import Environment

env = Environment(name="Helper_Environment")
print(f"Environment '{env.name}' created successfully.")

helper_agent = Agent(name="Helper_Agent", capabilities=["greeting", "answer_question"])
print(f"Agent '{helper_agent.name}' created")
print("Lets see what happens when the agent tries to run a cycle before being added to an environment:")
helper_agent.run_cycle()

print("Now, adding the agent to the environment.")
env.add_agent(helper_agent)
print("\n --- SIMULATION START --- ")
env.update_state("user_input", "Hello there!")

helper_agent.run_cycle()
print(" --- SIMULATION END --- \n")
