from framework.agent import Agent
from framework.environment import Environment

env = Environment(name="Helper_Environment")
helper_agent = Agent(name = "Helper_Agent", capabilities=["greeting","answer_question","clarify"] )
env.add_agent(helper_agent)

print("--- Agent Simulation Started ---")
print("Type 'quit' to exit.")
print("-"*20)

#create an interactive loop
while True:
    #gets user input
    user_input = input("You: ")

    #check for exist condition
    if user_input.lower() == "quit":
        print("Exiting simulation. Goodbye!")
        break

    #update the environment state with the user'ss input
    env.update_state("user_input", user_input)
    #run one full cycle of agent
    helper_agent.run_cycle()

    print(f"[DEBUG] Agent Memory: {helper_agent.memory_system.get_all()}")
    print("-"*20)

print("--- Agent Simulation Ended ---")

#C:\Users\MSII\Desktop\my_agentic_framework\venv\Scripts\python.exe main.py
 