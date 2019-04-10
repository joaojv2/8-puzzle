import argparse
import resource
import time

from Puzzle import Puzzle
from Solver import Solver


def export(result: tuple, total_time: float):
    file = open('output.txt', 'w')
    file.write("path_to_goal: " + str(result[0]))
    file.write("\ncost_of_path: " + str(len(result[0])))
    file.write("\nnodes_expanded: " + str(result[3]))
    file.write("\nfringe_size: " + str(len(result[2])))
    file.write("\nmax_fringe_size: " + str(result[5]))
    file.write("\nsearch_depth: " + str(result[1].depth))
    file.write("\nmax_search_depth: " + str(result[4]))
    file.write("\nrunning_time: " + format(total_time, '.8f'))
    file.write("\nmax_ram_usage: " + format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000.0, '.8f'))
    file.close()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('algorithm')
    parser.add_argument('board')

    args = parser.parse_args()

    initial_board: list = [int(e) for e in args.board.split(",")]
    goal_board: list = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    root_puzzle: Puzzle = Puzzle(initial_board, goal_board)
    solver: Solver = Solver()

    function_map: dict = {
        'bfs': solver.breadth_first_search,
        'dfs': solver.depth_first_search,
        'idfs': solver.iterative_depth_first_search,
        'ast': solver.a_star,
        'gfs': solver.best_first_search
    }

    start_time: float = time.time()

    result: tuple = function_map[args.algorithm](root_puzzle)

    stop_time: float = time.time()

    export(result, stop_time - start_time)


if __name__ == '__main__':
    main()
