from Puzzle import Puzzle


class Heuristic:

    @staticmethod
    def manhattan_distance(puzzle: Puzzle) -> int:
        return sum(abs(b % puzzle.width - g % puzzle.width) + abs(b // puzzle.width - g // puzzle.width)
                   for b, g in ((puzzle.state.index(i), puzzle.goal_state.index(i)) for i in range(1, puzzle.size)))
