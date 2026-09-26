# Task1 class ModelBasedReflexAgent:
class ModelBasedReflexAgent:

    def __init__(self):
        self.internal_state = {"ac_status": "OFF"}

    def perceive_and_act(self, temperature):
        if temperature > 26:
            self.internal_state["ac_status"] = "ON"
            action = "Turn AC ON"
        else:
            self.internal_state["ac_status"] = "OFF"
            action = "Turn AC OFF"

        return action


agent = ModelBasedReflexAgent()

print(agent.perceive_and_act(30))
print(agent.perceive_and_act(22))
# Task 2class ModelBasedReflexAgent:
class ModelBasedReflexAgent:

    def __init__(self):
        self.internal_state = {"ac_status": "OFF"}

    def perceive_and_act(self, temperature):
        if temperature > 26:
            self.internal_state["ac_status"] = "ON"
            action = "Turn AC ON"
        else:
            self.internal_state["ac_status"] = "OFF"
            action = "Turn AC OFF"

        return action


agent = ModelBasedReflexAgent()

temperatures = [18, 22, 25, 25, 19]

for temperature in temperatures:
    action = agent.perceive_and_act(temperature)
    print(temperature, "->", action)
