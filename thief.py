from agent import Agent
from agent_type import AgentType

class Thief(Agent):
    def __init__(self, agent_id, graph, start_node=None):
        super().__init__(agent_id, graph, start_node)
        self.agent_type = AgentType.THIEF

    def move(self, agents_positions=None):
        """
        Move the police agent to a random neighbor or get information about the thief's position every 5 turns.

        :param agent_positions: The position of the agents. It's an dictionary from agent_id as key to (node_id, agent_type) as value.
        """
        # TODO

        # Move as normal (can be modified to make more intelligent movement)
        return super().move()
