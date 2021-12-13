import os
import sys
from typing import List, Tuple


class Board:
    MARKED = -1

    def __init__(self, numbers: List[List[int]]) -> None:
        self._numbers = numbers

    def mark_number(self, number: int):
        for i, row in enumerate(self._numbers):
            for j, cell in enumerate(row):
                if cell == number:
                    self._numbers[i][j] = self.MARKED

    def has_won(self) -> bool:
        return self.check_rows() or self.check_columns()

    def check_rows(self) -> bool:
        for i, _ in enumerate(self._numbers):
            if self.check_list_as_marked(self._numbers[i]):
                return True
        return False

    def check_list_as_marked(self, row: List[int]) -> bool:
        for cell in row:
            if cell != self.MARKED:
                return False
        return True

    def check_columns(self) -> bool:
        for i, _ in enumerate(self._numbers[0]):
            if self.check_list_as_marked([row[i] for row in self._numbers]):
                return True
        return False

    def sum_of_unmarked_cells(self) -> int:
        return sum(
            [cell for row in self._numbers for cell in row if cell != self.MARKED]
        )


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


def create_boards(input_data: List[str]) -> List[Board]:
    boards = []
    numbers = []
    for line in input_data:
        if line == "\n":
            boards.append(Board(numbers))
            numbers = []
        else:
            valid_numbers = [int(el) for el in line.split(" ") if el != ""]
            numbers.append(valid_numbers)

    return boards


def retrieve_first_winning_board(
    boards: List[Board], numbers: List[int]
) -> Tuple[int, Board]:
    for _, number in enumerate(numbers):
        for board in boards:
            board.mark_number(number)
            if board.has_won():
                return number, board
    return None, None


def retrieve_last_winning_board(
    boards: List[Board], numbers: List[int]
) -> Tuple[int, Board]:
    boards_in_competition = [(board, False) for board in boards]
    nb_remaining_boards = len(boards_in_competition)
    for _, number in enumerate(numbers):
        for i, (board, has_already_won) in enumerate(boards_in_competition):
            if has_already_won:
                continue
            board.mark_number(number)
            if board.has_won():
                boards_in_competition[i] = (board, True)
                nb_remaining_boards -= 1
                if nb_remaining_boards == 0:
                    return number, board

    return None, None


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    numbers_input = read_input_file(f"{current_dir}/input-numbers.txt")
    boards_input = read_input_file(f"{current_dir}/input-boards.txt")

    numbers = [int(n) for n in numbers_input[0].split(",")]
    boards = create_boards(boards_input)

    if argv == "1":
        last_number, winning_board = retrieve_first_winning_board(boards, numbers)
        sum_of_unmarked_cells = winning_board.sum_of_unmarked_cells()
        print(
            f"The finale score is: ({last_number=}, {sum_of_unmarked_cells=}) -> {sum_of_unmarked_cells * last_number}"
        )
    elif argv == "2":
        last_number, last_winning_board = retrieve_last_winning_board(boards, numbers)
        sum_of_unmarked_cells = last_winning_board.sum_of_unmarked_cells()
        print(
            f"The finale score is: ({last_number=}, {sum_of_unmarked_cells=}) -> {sum_of_unmarked_cells * last_number}"
        )
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
