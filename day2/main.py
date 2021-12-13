import os
import sys
from typing import List, Tuple


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


def retrieve_horizontal_position_and_depth_part_one(
    content: List[str],
) -> Tuple[int, int]:
    horizontal_pos = 0
    depth = 0
    for line in content:
        [instruction, unit] = line.split(" ")
        if instruction == "forward":
            horizontal_pos += int(unit)
        elif instruction == "up":
            depth -= int(unit)
        elif instruction == "down":
            depth += int(unit)

    return horizontal_pos, depth


def retrieve_horizontal_position_and_depth_part_two(
    content: List[str],
) -> Tuple[int, int]:
    horizontal_pos = 0
    depth = 0
    aim = 0
    for line in content:
        [instruction, unit] = line.split(" ")
        if instruction == "forward":
            horizontal_pos += int(unit)
            depth += int(unit) * aim
        elif instruction == "up":
            aim -= int(unit)
        elif instruction == "down":
            aim += int(unit)

    return horizontal_pos, depth


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        horizontal_pos, depth = retrieve_horizontal_position_and_depth_part_one(content)
        print(
            f"The final position is [{horizontal_pos}, {depth}] -> {horizontal_pos * depth}"
        )
    elif argv == "2":
        horizontal_pos, depth = retrieve_horizontal_position_and_depth_part_two(content)
        print(
            f"The final position is [{horizontal_pos}, {depth}] -> {horizontal_pos * depth}"
        )
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
