import os
import sys
from posixpath import split
from typing import Dict, List, Tuple


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


def find_pairs_in_polymer(
    pairs_in_polymer: Dict[str, int],
    resulting_pairs: Dict[str, Tuple[str, str]],
    pair_insertions: Dict[str, str],
    elements_in_polymer: Dict[str, int]
) -> Dict[str, int]:

    new_pairs_in_polymer = {}

    for pair, occurrences in pairs_in_polymer.items():
        for resulting_pair in resulting_pairs[pair]:
            new_pairs_in_polymer[resulting_pair] = new_pairs_in_polymer.get(resulting_pair, 0) + occurrences
        new_element = pair_insertions[pair]
        elements_in_polymer[new_element] = elements_in_polymer.get(new_element, 0) + occurrences

    return new_pairs_in_polymer


def part_two(polymer_template: str, pair_insertions: Dict[str, str]) -> str:
    resulting_pairs = {
        pair: (pair[0] + insertion, insertion + pair[1])
        for pair, insertion in pair_insertions.items()
    }
    pairs_in_polymer = {
        pair: polymer_template.count(pair)
        for pair in pair_insertions.keys()
        if polymer_template.count(pair) != 0
    }
    elements_in_polymer = {
        element: polymer_template.count(element)
        for element in polymer_template
    }

    for _ in range(40):
        pairs_in_polymer = find_pairs_in_polymer(pairs_in_polymer, resulting_pairs, pair_insertions, elements_in_polymer)

    most_occurring_element = max(elements_in_polymer, key=elements_in_polymer.get)
    least_occurring_element = min(elements_in_polymer, key=elements_in_polymer.get)

    print(
        f"Part two: {elements_in_polymer[most_occurring_element] - elements_in_polymer[least_occurring_element]}"
    )



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
