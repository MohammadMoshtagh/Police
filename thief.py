from agent import Agent
from agent_type import AgentType

class Thief(Agent):
    def __init__(self, agent_id, graph, start_node=None):
        super().__init__(agent_id, graph, start_node)
        self.agent_type = AgentType.THIEF

    def move(self, agents_positions=None):
        """
        Move the police agent to a random neighbor or get information about the thief's position every 5 turns.

        :param agents_positions: The position of the agents.
        It's a dictionary with "polices" and "thieves" as keys and the value is the list of positions.
        """
        # TODO

        # Move as normal (can be modified to make more intelligent movement)
        return super().move()
