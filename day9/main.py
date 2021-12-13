import os
import sys
from functools import reduce
from typing import List, Tuple


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


def content_to_matrix(content: List[str]) -> List[List[int]]:
    matrix = []
    row = []
    for line in content:
        for char in line.strip("\n"):
            row.append(int(char))
        matrix.append(row)
        row = []
    return matrix


def is_low_point(
    point: int, left: int = 10, right: int = 10, top: int = 10, bottom: int = 10
) -> bool:
    if point < left and point < right and point < top and point < bottom:
        return True
    return False


def find_low_points(content: List[str]) -> List[int]:
    matrix = content_to_matrix(content)
    low_points = []
    for x, row in enumerate(matrix):
        for y, _ in enumerate(row):
            left = matrix[x - 1][y] if x != 0 else 10
            right = matrix[x + 1][y] if x != len(matrix) - 1 else 10
            top = matrix[x][y - 1] if y != 0 else 10
            bottom = matrix[x][y + 1] if y != len(row) - 1 else 10
            if is_low_point(matrix[x][y], left, right, top, bottom):
                low_points.append(matrix[x][y])

    return low_points


def derive_risk_level(low_points: List[int]) -> int:
    return reduce(lambda x, y: x + y + 1, low_points, 0)


def find_low_points_coordinates(content: List[str]) -> List[Tuple[int, int]]:
    matrix = content_to_matrix(content)
    low_points_coordinates = []
    for x, row in enumerate(matrix):
        for y, _ in enumerate(row):
            left = matrix[x - 1][y] if x != 0 else 10
            right = matrix[x + 1][y] if x != len(matrix) - 1 else 10
            top = matrix[x][y - 1] if y != 0 else 10
            bottom = matrix[x][y + 1] if y != len(row) - 1 else 10
            if is_low_point(matrix[x][y], left, right, top, bottom):
                low_points_coordinates.append((x, y))

    return low_points_coordinates


def is_in_matrix(x: int, y: int, matrix: List[List[int]]) -> bool:
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def compute_island_size(
    matrix: List[List[int]], visited: list[list[bool]], x: int, y: int
) -> int:
    visited[x][y] = True
    island_size = 1
    rows_to_visit = [-1, 0, 0, 1]
    cols_to_visit = [0, -1, 1, 0]
    for row_offset, col_offset in zip(rows_to_visit, cols_to_visit):
        if (
            is_in_matrix(x + row_offset, y + col_offset, matrix)
            and not visited[x + row_offset][y + col_offset]
            and matrix[x + row_offset][y + col_offset] != 9
        ):
            island_size += compute_island_size(
                matrix, visited, x + row_offset, y + col_offset
            )

    return island_size


def find_largest_islands(
    content: List[str], low_points_coordinates: List[Tuple[int, int]]
) -> List[int]:
    islands_sizes = []
    matrix = content_to_matrix(content)
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for x, y in low_points_coordinates:
        if not visited[x][y]:
            islands_sizes.append(compute_island_size(matrix, visited, x, y))
    return sorted(islands_sizes)[-3:]


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        low_points = find_low_points(content)
        risk_level = derive_risk_level(low_points)
        print(f"Risk level: {risk_level}")
    elif argv == "2":
        low_points_coordinates = find_low_points_coordinates(content)
        largest_islands = find_largest_islands(content, low_points_coordinates)
        print(
            f"Sizes of 3 largest islands: {largest_islands} -> {reduce(lambda x, y: x * y, largest_islands)}"
        )
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
