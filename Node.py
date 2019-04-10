from Puzzle import Puzzle


class Node:

    def __init__(self, puzzle: Puzzle, move: str = '', depth: int = 0, cost: int = 0, parent=None, key=None):
        self.puzzle: Puzzle = puzzle
        self.move: str = move
        self.depth: int = depth
        self.cost: int = cost
        self.parent: Node = parent
        self.key: int = key

    @property
    def map(self):
        return self.puzzle.map

    @property
    def expand(self) -> list:
        neighbors: list = [Node(self.puzzle.move_right(), 'RIGHT', self.depth + 1, self.cost + 1, self),
                           Node(self.puzzle.move_left(), 'LEFT', self.depth + 1, self.cost + 1, self),
                           Node(self.puzzle.move_up(), 'UP', self.depth + 1, self.cost + 1, self),
                           Node(self.puzzle.move_down(), 'DOWN', self.depth + 1, self.cost + 1, self)]

        return [neighbor for neighbor in neighbors if neighbor.puzzle]

    def __lt__(self, other):
        return self.map < other.map
