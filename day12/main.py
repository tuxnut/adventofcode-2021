import os
import sys
from typing import Dict, List, Set


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


def create_cave_system(content: List[str]) -> Dict[str, List[str]]:
    cave = {}
    for line in content:
        start, end = line.strip().split("-")
        cave[start] = cave.get(start, []) + [end]
        cave[end] = cave.get(end, []) + [start]
    return cave


def remove_cave_from_system(
    cave_name: str, cave_system: Dict[str, List[str]]
) -> Dict[str, List[str]]:
    return {
        cave: [
            connected_cave
            for connected_cave in connections
            if connected_cave != cave_name
        ]
        for cave, connections in cave_system.items()
        if cave != cave_name
    }


def complete_path(current_cave: str, paths: List[List[str]], path_index: int):
    if path_index == 0:
        paths.append([current_cave])
    else:
        if paths[-1][-1] == "end":
            paths.append(paths[-1][:path_index] + [current_cave])
        else:
            paths[-1].append(current_cave)


def find_paths(
    current_cave: str,
    cave_system: Dict[str, List[str]],
    paths: List[List[str]],
    path_index: int,
) -> int:
    if cave_system[current_cave]:
        complete_path(current_cave, paths, path_index)

    if current_cave == "end":
        return 1
    else:
        new_cave_system = (
            remove_cave_from_system(current_cave, cave_system)
            if current_cave.islower()
            else cave_system
        )
        return sum(
            [
                find_paths(cave, new_cave_system, paths, path_index + 1)
                for cave in cave_system[current_cave]
            ]
        )


def part_one(content: List[str]):
    cave_system = create_cave_system(content)
    paths = []
    print(find_paths("start", cave_system, paths, 0))
    # for p in paths:
    #     print(p)


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        part_one(content)
    elif argv == "2":
        pass
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
