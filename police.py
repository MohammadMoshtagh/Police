from agent import Agent

class Police(Agent):
    def __init__(self, graph, start_node=None):
        super().__init__(graph, start_node)
        self.turn_counter = 0

    def move(self, thief_position=None):
        """
        Move the police agent to a random neighbor or get information about the thief's position every 5 turns.

        :param thief_position: The position of the thief. Only used every 5 turns.
        """
        self.turn_counter += 1

        # Receive information about the thief's position every 5 turns
        if self.turn_counter % 5 == 0 and thief_position is not None:
            print(f"Turn {self.turn_counter}: Police receives information that the thief is at node {thief_position}")

        # Move as normal (can be modified to make more intelligent movement)
        return super().move()