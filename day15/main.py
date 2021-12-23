import os
import sys
from heapq import heappop, heappush
from typing import Any, Dict, Generator, List, NamedTuple, Optional, Tuple

Position = NamedTuple("Position", [("x", int), ("y", int)])
Maze = List[List[int]]


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = list(f)

    return content


class PriorityQueue:
    def __init__(self):
        self.elements: List[Tuple[float, Any]] = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item: Any, priority: float):
        heappush(self.elements, (priority, item))

    def pop(self) -> Any:
        return heappop(self.elements)[1]


def create_maze(content: List[str]) -> Maze:
    return [[int(cost) for cost in line.strip()] for line in content]


def get_neighbors(position: Position, maze: Maze) -> Generator[Position, None, None]:
    col = [-1, 0, 0, 1]
    row = [0, -1, 1, 0]

    for offset_col, offet_row in zip(col, row):
        if 0 <= position.x + offset_col < len(
            maze
        ) and 0 <= position.y + offet_row < len(maze[0]):
            yield Position(position.x + offset_col, position.y + offet_row)


def compute_cost(position: Position, maze: Maze) -> int:
    return maze[position.x][position.y]


def heuristic(a: Position, b: Position) -> float:
    return abs(a.x - b.x) + abs(a.y - b.y)


def a_star(
    maze: Maze, start: Position, end: Position
) -> Dict[Position, Optional[Position]]:
    opened = PriorityQueue()
    opened.put(start, 0)
    reverse_path: Dict[Position, Optional[Position]] = {}
    cost_so_far: Dict[Position, int] = {}
    reverse_path[start] = None
    cost_so_far[start] = 0

    while not opened.empty():
        current: Position = opened.pop()

        if current == end:
            break

        for neighbor in get_neighbors(current, maze):
            new_cost = cost_so_far[current] + compute_cost(neighbor, maze)
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, end)
                opened.put(neighbor, priority)
                reverse_path[neighbor] = current

    return reverse_path


def compute_path(
    reverse_path: Dict[Position, Optional[Position]], last_position: Position
) -> List[Position]:
    path: List[Position] = [last_position]
    previous_position = reverse_path[last_position]
    while previous_position:
        path.append(previous_position)
        previous_position = reverse_path[previous_position]

    path.reverse()
    return path


def compute_path_cost(path: List[Position], maze: Maze) -> int:
    starting_position = path[0]
    return (
        sum(maze[position.x][position.y] for position in path)
        - maze[starting_position.x][starting_position.y]
    )


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        maze = create_maze(content)
        reverse_path = a_star(
            maze, Position(0, 0), Position(len(maze) - 1, len(maze[0]) - 1)
        )
        path = compute_path(reverse_path, Position(len(maze) - 1, len(maze[0]) - 1))
        total_cost = compute_path_cost(path, maze)
        print(total_cost)
    elif argv == "2":
        pass
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
