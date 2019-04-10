class Puzzle:

    def __init__(self, state: list, goal: list):
        self.size: int = len(state)
        self.width: int = int(self.size ** 0.5)
        self.state: list = state
        self.goal_state: list = goal

    @property
    def map(self) -> str:
        return ''.join(str(x) for x in self.state)

    def __eq__(self, other):
        return self.map == other.map

    def move_right(self):
        index: int = self.state.index(0)

        if index % self.width < self.width - 1:
            new_state: list = self.state[:]
            new_state[index], new_state[index + 1] = new_state[index + 1], new_state[index]

            return Puzzle(new_state, self.goal_state)

        else:
            return None

    def move_left(self):
        index: int = self.state.index(0)

        if index % self.width > 0:
            new_state: list = self.state[:]
            new_state[index], new_state[index - 1] = new_state[index - 1], new_state[index]

            return Puzzle(new_state, self.goal_state)

        else:
            return None

    def move_up(self):
        index: int = self.state.index(0)

        if index - self.width >= 0:
            new_state: list = self.state[:]
            new_state[index], new_state[index - self.width] = new_state[index - self.width], new_state[index]

            return Puzzle(new_state, self.goal_state)

        else:
            return None

    def move_down(self):
        index: int = self.state.index(0)

        if index + self.width < len(self.state):
            new_state: list = self.state[:]
            new_state[index], new_state[index + self.width] = new_state[index + self.width], new_state[index]

            return Puzzle(new_state, self.goal_state)

        else:
            return None
