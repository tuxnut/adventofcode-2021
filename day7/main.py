import os
import sys
from statistics import mean, median
from typing import List


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


def part_one(content: List[str]):
    crabs_position = [int(x) for line in content for x in line.split(",")]
    med = median(crabs_position)
    cost_med = sum([abs(x - med) for x in crabs_position])
    print(f"Fuel used: {cost_med}")


def fuel_burnt(start: int, destination: int) -> int:
    n = abs(destination - start)
    return (n + 1) * n / 2


def part_two(content: List[str]):
    crabs_position = [int(x) for line in content for x in line.split(",")]
    average = int(mean(crabs_position)) - 2
    cost_averages = []
    for i in range(average, average + 4):
        cost_averages.append(int(sum([fuel_burnt(x, i) for x in crabs_position])))
    print(f"Fuel used: {min(cost_averages)}")


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
