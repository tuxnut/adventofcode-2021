import os
import sys
from typing import List


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


def count_increased_measurements(measurements: List[str]) -> int:
    count = 0
    for idx, value in enumerate(measurements):
        if idx == 0:
            continue
        last_measure = int(measurements[idx - 1])
        current_measure = int(value)
        count = count + 1 if current_measure > last_measure else count

    return count


def count_increased_three_measurements(measurements: List[str]) -> int:
    count = 0
    for idx, value in enumerate(measurements):
        if idx < 3:
            continue
        sum_last_three_measures = (
            int(measurements[idx - 1])
            + int(measurements[idx - 2])
            + int(measurements[idx - 3])
        )
        sum_current_three_measures = (
            int(value) + int(measurements[idx - 1]) + int(measurements[idx - 2])
        )
        count = (
            count + 1 if sum_current_three_measures > sum_last_three_measures else count
        )

    return count


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        number_of_increased_measurements = count_increased_measurements(content)
        print(f"Number of increased measurements: {number_of_increased_measurements}")
    elif argv == "2":
        number_of_increased_measurements = count_increased_three_measurements(content)
        print(
            f"Number of increased three measurements: {number_of_increased_measurements}"
        )
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
