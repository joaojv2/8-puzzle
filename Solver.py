import itertools
from collections import deque
from heapq import heappush, heappop, heapify

from Heuristic import Heuristic
from Node import Node
from Puzzle import Puzzle


class Solver:

    def __init__(self):
        self.expanded_nodes: int = 0
        self.max_search_depth: int = 0
        self.max_frontier_size: int = 0

    @staticmethod
    def backtrace(goal_node: Node):
        current_node: Node = goal_node
        moves: list = []

        while current_node.parent is not None:
            moves.append(current_node.move)
            current_node = current_node.parent

        return moves

    """
        this function 
    """

    def breadth_first_search(self, root_puzzle: Puzzle) -> tuple:
        root_node: Node = Node(root_puzzle)
        explored_nodes, queue = set(), deque([root_node])

        while queue:

            current_node: Node = queue.popleft()
            explored_nodes.add(current_node.map)

            if current_node.puzzle.state == root_puzzle.goal_state:
                return self.backtrace(current_node), current_node, queue, self.expanded_nodes, self.max_search_depth, \
                       self.max_frontier_size

            for neighbor in current_node.expand:

                self.expanded_nodes += 1

                if neighbor.map not in explored_nodes:
                    queue.append(neighbor)
                    explored_nodes.add(neighbor.map)

                    if neighbor.depth > self.max_search_depth:
                        self.max_search_depth += 1

            if len(queue) > self.max_frontier_size:
                self.max_frontier_size = len(queue)

    """
        this function 
    """
    def depth_first_search(self, root_puzzle: Puzzle) -> tuple:
        root_node: Node = Node(root_puzzle)
        explored_nodes, stack = set(), list([root_node])

        while stack:

            current_node: Node = stack.pop()
            explored_nodes.add(current_node.map)

            if current_node.puzzle.state == root_puzzle.goal_state:
                return self.backtrace(current_node), current_node, stack, self.expanded_nodes, self.max_search_depth, \
                       self.max_frontier_size

            for neighbor in reversed(current_node.expand):

                self.expanded_nodes += 1

                if neighbor.map not in explored_nodes:
                    stack.append(neighbor)
                    explored_nodes.add(neighbor.map)

                    if neighbor.depth > self.max_search_depth:
                        self.max_search_depth += 1

            if len(stack) > self.max_frontier_size:
                self.max_frontier_size = len(stack)

    """
        this function
    """
    def iterative_depth_first_search(self, root_puzzle: Puzzle) -> tuple:
        count: int = 1

        while True:

            root_node: Node = Node(root_puzzle)
            explored_nodes, stack = set(), list([root_node])

            while stack:

                current_node: Node = stack.pop()
                explored_nodes.add(current_node.map)

                if current_node.puzzle.state == root_puzzle.goal_state:
                    return self.backtrace(
                        current_node), current_node, stack, self.expanded_nodes, self.max_search_depth, \
                           self.max_frontier_size, count

                if current_node.depth < count:
                    for neighbor in reversed(current_node.expand):

                        self.expanded_nodes += 1

                        if neighbor.map not in explored_nodes:
                            stack.append(neighbor)
                            explored_nodes.add(neighbor.map)

                            if neighbor.depth > self.max_search_depth:
                                self.max_search_depth += 1

                    if len(stack) > self.max_frontier_size:
                        self.max_frontier_size = len(stack)

            count += 1

    """
        this function
    """
    def a_star(self, root_puzzle: Puzzle) -> tuple:
        explored_nodes, heap, heap_entry, counter = set(), list(), {}, itertools.count()

        key: int = Heuristic.manhattan_distance(root_puzzle)
        root_node: Node = Node(root_puzzle, key=key)

        entry: tuple = (key, root_node)
        heappush(heap, entry)

        heap_entry[root_node.map] = entry

        while heap:

            current_entry = heappop(heap)
            explored_nodes.add(current_entry[1].map)

            if current_entry[1].puzzle.state == root_puzzle.goal_state:
                return self.backtrace(current_entry[1]), current_entry[1], heap, self.expanded_nodes, \
                       self.max_search_depth, self.max_frontier_size

            for neighbor in current_entry[1].expand:

                self.expanded_nodes += 1

                neighbor.key = neighbor.cost + Heuristic.manhattan_distance(neighbor.puzzle)
                entry = (neighbor.key, neighbor)

                if neighbor.map not in explored_nodes:
                    heappush(heap, entry)
                    explored_nodes.add(neighbor.map)
                    heap_entry[neighbor.map] = entry

                    if neighbor.depth > self.max_search_depth:
                        self.max_search_depth += 1

                elif neighbor.map in heap_entry and neighbor.key < heap_entry[neighbor.map][1].key:
                    heap_index = heap.index((heap_entry[neighbor.map][1].key,
                                            heap_entry[neighbor.map][1]))

                    heap[int(heap_index)] = entry
                    heap_entry[neighbor.map] = entry
                    heapify(heap)

            if len(heap) > self.max_frontier_size:
                self.max_frontier_size = len(heap)

    """
        this function
    """
    def best_first_search(self, root_puzzle: Puzzle) -> tuple:
        explored_nodes, heap, counter = set(), list(), itertools.count()

        key: int = Heuristic.manhattan_distance(root_puzzle)
        root_node: Node = Node(root_puzzle, key=key)

        entry: tuple = (key, root_node)
        heappush(heap, entry)

        while heap:

            current_entry = heappop(heap)

            explored_nodes.add(current_entry[1].map)

            if current_entry[1].puzzle.state == root_puzzle.goal_state:
                return self.backtrace(current_entry[1]), current_entry[1], heap, self.expanded_nodes, \
                       self.max_search_depth, self.max_frontier_size

            for neighbor in current_entry[1].expand:

                self.expanded_nodes += 1

                neighbor.key = neighbor.cost + Heuristic.manhattan_distance(neighbor.puzzle)
                entry = (neighbor.key, neighbor)

                if neighbor.map not in explored_nodes:
                    heappush(heap, entry)
                    explored_nodes.add(neighbor.map)

                    if neighbor.depth > self.max_search_depth:
                        self.max_search_depth += 1

            if len(heap) > self.max_frontier_size:
                self.max_frontier_size = len(heap)
