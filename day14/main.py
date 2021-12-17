import os
import sys
from posixpath import split
from typing import Dict, List


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


def process_polymer(polymer: str, pair_insertions: Dict[str, str], steps: int) -> str:
    polymer_tmp = polymer
    for _ in range(steps):
        new_polymer = polymer_tmp[0]
        for element in polymer_tmp[1:]:
            pair = new_polymer[-1] + element
            if pair in pair_insertions:
                new_polymer += pair_insertions[pair] + element
            else:
                new_polymer += element
        print(f"{len(new_polymer) == len(polymer_tmp) * 2 - 1}")
        polymer_tmp = new_polymer
    return new_polymer


def count_elements(polymer: str) -> Dict[str, int]:
    occurrences = {}
    for element in polymer:
        occurrences[element] = occurrences.get(element, 0) + 1
    return occurrences


def part_one(polymer_template: str, pair_insertions: Dict[str, str]) -> str:
    polymer = process_polymer(polymer_template, pair_insertions, 10)
    elements_count = count_elements(polymer)
    most_occurring_element = max(elements_count, key=elements_count.get)
    least_occurring_element = min(elements_count, key=elements_count.get)

    print(
        f"Part one: {elements_count[most_occurring_element] - elements_count[least_occurring_element]}"
    )


def part_two(polymer_template: str, pair_insertions: Dict[str, str]) -> str:
    pass


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")
    polymer_template = content[0].strip()
    pair_insertions = {}
    for line in content[2:]:
        pair, insertion = line.strip().split(" -> ")
        pair_insertions[pair] = insertion

    if argv == "1":
        part_one(polymer_template, pair_insertions)
    elif argv == "2":
        part_two(polymer_template, pair_insertions)
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
