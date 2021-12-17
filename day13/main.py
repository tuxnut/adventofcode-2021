import os
import sys
from typing import List, Set, Tuple


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


def fold(
    board_with_dots: Set[Tuple[int, int]], fold_instruction: Tuple[str, int]
) -> Set[Tuple[int, int]]:
    axe = 0 if fold_instruction[0] == "x" else 1
    new_board = set()
    for dot in board_with_dots:
        new_dot = list(dot)
        if dot[axe] > fold_instruction[1]:
            new_dot[axe] = 2 * fold_instruction[1] - dot[axe]
        new_board.add(tuple(new_dot))

    return new_board


def print_board(board: Set[Tuple[int, int]]) -> None:
    min_x = min(x for x, _ in board)
    max_x = max(x for x, _ in board)
    min_y = min(y for _, y in board)
    max_y = max(y for _, y in board)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in board:
                print("#", end="")
            else:
                print(" ", end="")
        print()


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")
    board_with_dots = set()
    fold_instructions = []
    for line in content:
        if line.startswith("fold along"):
            axe, value = line.strip("fold along").strip().split("=")
            fold_instructions.append((axe, int(value)))
        elif line != "\n":
            board_with_dots.add(tuple([int(x) for x in line.strip().split(",")]))

    if argv == "1":
        folded_board = fold(board_with_dots, fold_instructions[0])
        print(len(folded_board))
    elif argv == "2":
        for instruction in fold_instructions:
            board_with_dots = fold(board_with_dots, instruction)
        print_board(board_with_dots)
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
