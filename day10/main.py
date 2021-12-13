import os
import sys
from typing import List


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


closing_tag_of = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

illegal_char_score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

opening_chars = ["(", "[", "{", "<"]

closing_character_scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def get_first_illegal_char_score(line: str) -> int:
    score = 0
    stack = []
    for char in line:
        if char == "\n":
            continue
        elif char in opening_chars:
            stack.append(char)
        else:
            if char != closing_tag_of[stack[-1]]:
                return illegal_char_score[char]
            else:
                stack.pop()
    return score


def part_one(content: List[str]):
    score = 0
    for line in content:
        score += get_first_illegal_char_score(line)
    return score


def complete_closing_tags(stack: List[str]) -> List[str]:
    result = []
    while len(stack) > 0:
        result.append(closing_tag_of[stack.pop()])
    return result


def complete_line(line: str) -> str:
    stack = []
    for char in line:
        if char == "\n":
            break
        elif char in opening_chars:
            stack.append(char)
        else:
            if char != closing_tag_of[stack[-1]]:
                return []
            else:
                stack.pop()
    return complete_closing_tags(stack)


def get_rest_of_line_score(line: str) -> int:
    score = 0
    for char in line:
        score *= 5
        score += closing_character_scores[char]
    return score


def part_two(content: List[str]) -> int:
    score = []
    for line in content:
        rest_of_line = complete_line(line)
        if len(rest_of_line) > 0:
            score.append(get_rest_of_line_score(rest_of_line))

    return sorted(score)[len(score) // 2]


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        illegal_char_score = part_one(content)
        print(illegal_char_score)
    elif argv == "2":
        middle_score = part_two(content)
        print(middle_score)
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
