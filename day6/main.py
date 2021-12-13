import os
import sys
from collections import deque
from typing import List

TIMER_RESET = 6
TIMER_FOR_NEW_LANTERFISH = 8


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


def retrieve_lanterfishes_timers(content: List[str]) -> List[int]:
    timers = []
    for line in content:
        timers.extend([int(n) for n in line.split(",")])

    return timers


def part_one(content: List[str]):
    iterations = 80
    lanternfishes = retrieve_lanterfishes_timers(content)
    for _ in range(iterations):
        new_lanterfishes = []
        for position, lanternfish_timer in enumerate(lanternfishes):
            if lanternfish_timer == 0:
                new_lanterfishes.append(TIMER_FOR_NEW_LANTERFISH)
                lanternfishes[position] = TIMER_RESET
            else:
                lanternfishes[position] = lanternfishes[position] - 1
        lanternfishes.extend(new_lanterfishes)
    print(f"{len(lanternfishes)} lanternfishes after {iterations} iterations")


def count_lanternfish_children(lanternfish_timer: int, iterations_left: int) -> int:
    if iterations_left - lanternfish_timer <= 0:
        return 0
    else:
        lanternfish_counter = 1
        for iteration_at_child in range(
            iterations_left - lanternfish_timer, 0, -TIMER_RESET
        ):
            lanternfish_counter += count_lanternfish_children(
                TIMER_FOR_NEW_LANTERFISH, iteration_at_child
            )
        return lanternfish_counter


def part_two(content: List[str]):
    iterations = 256
    lanternfishes = retrieve_lanterfishes_timers(content)
    lanternfishes_by_timer = deque(
        [lanternfishes.count(timer) for timer in range(TIMER_FOR_NEW_LANTERFISH + 1)]
    )
    for _ in range(iterations):
        lanternfishes_by_timer.rotate(-1)
        lanternfishes_by_timer[TIMER_RESET] += lanternfishes_by_timer[
            TIMER_FOR_NEW_LANTERFISH
        ]

    print(f"{sum(lanternfishes_by_timer)} lanternfishes after {iterations} iterations")


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
