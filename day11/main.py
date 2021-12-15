import os
import sys
from typing import List


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


def create_octopus_energy_matrix(content: List[str]) -> List[List[int]]:
    matrix = []
    for line in content:
        row = [int(char) for char in line if char != "\n"]
        matrix.append(row)

    return matrix


def is_in_matrix(matrix: List[List[int]], x: int, y: int) -> bool:
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def flash_octopus(matrix: List[List[int]], x: int, y: int) -> int:
    rows_to_visit = [-1, -1, -1, 0, 0, 1, 1, 1]
    cols_to_visit = [-1, 0, 1, -1, 1, -1, 0, 1]
    octopus_flashes = 1
    for row_offset, col_offset in zip(rows_to_visit, cols_to_visit):
        if (
            is_in_matrix(matrix, x + row_offset, y + col_offset)
            and not matrix[x + row_offset][y + col_offset] > 9
        ):
            matrix[x + row_offset][y + col_offset] += 1
            if matrix[x + row_offset][y + col_offset] > 9:
                octopus_flashes += flash_octopus(matrix, x + row_offset, y + col_offset)

    return octopus_flashes


def reset_flashed_octopus(matrix: List[List[int]]):
    for x, row in enumerate(matrix):
        for y, _ in enumerate(row):
            matrix[x][y] = 0 if matrix[x][y] > 9 else matrix[x][y]


def count_octopus_flashes_in_step(matrix: List[List[int]]) -> int:
    octopus_flashes = 0
    for x, row in enumerate(matrix):
        for y, _ in enumerate(row):
            if matrix[x][y] > 9:
                continue
            matrix[x][y] += 1
            if matrix[x][y] > 9:
                octopus_flashes += flash_octopus(matrix, x, y)

    return octopus_flashes


def count_octopus_flashes(matrix: List[List[int]], steps: int) -> int:
    total_flashes = 0

    for _ in range(steps):
        total_flashes += count_octopus_flashes_in_step(matrix)
        reset_flashed_octopus(matrix)
    return total_flashes


def part_one(content: List[str]):
    matrix = create_octopus_energy_matrix(content)
    print(f"Nombre de flashs: {count_octopus_flashes(matrix, 100)}")


def first_simultaneous_flash(matrix: List[List[int]]) -> int:
    are_octopuses_all_flashing = False
    step = 0
    while not are_octopuses_all_flashing:
        step += 1
        reset_flashed_octopus(matrix)
        flashes = count_octopus_flashes_in_step(matrix)
        if flashes == len(matrix) * len(matrix[0]):
            are_octopuses_all_flashing = True

    return step


def part_two(content: List[str]):
    matrix = create_octopus_energy_matrix(content)
    print(f"Flash simultané au step: : {first_simultaneous_flash(matrix)}")


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        part_one(content)
    elif argv == "2":
        part_two(content)
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
