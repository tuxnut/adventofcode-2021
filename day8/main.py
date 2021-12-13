import os
import sys
from typing import Dict, List, NamedTuple


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


nb_segments_by_digit = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}


def part_one(content: List[str]):
    cpt = 0
    for line in content:
        output = line.split("|")[-1].strip()
        for segments in output.split(" "):
            if (
                len(segments) == nb_segments_by_digit[1]
                or len(segments) == nb_segments_by_digit[4]
                or len(segments) == nb_segments_by_digit[7]
                or len(segments) == nb_segments_by_digit[8]
            ):
                cpt += 1
    print(cpt)


def contains(container: str, contained: str) -> bool:
    for segment in contained:
        if segment not in container:
            return False
    return True


def derive_segments_to_digit(segments: str) -> Dict[str, int]:
    segments_to_digit: Dict[str, int] = {}
    # find 1, 4, 7 and 8 in first pass
    for value in segments.split(" "):
        current_segments = "".join(sorted(value))
        if len(value) == nb_segments_by_digit[1]:
            segments_to_digit[current_segments] = 1
        elif len(value) == nb_segments_by_digit[4]:
            segments_to_digit[current_segments] = 4
        elif len(value) == nb_segments_by_digit[7]:
            segments_to_digit[current_segments] = 7
        elif len(value) == nb_segments_by_digit[8]:
            segments_to_digit[current_segments] = 8

    digit_to_segments: Dict[int, List[str]] = dict(
        (value, key) for key, value in segments_to_digit.items()
    )
    # find 0, 6, 9 in second pass
    for value in segments.split(" "):
        if len(value) == nb_segments_by_digit[0]:
            current_segments = "".join(sorted(value))
            if not contains(current_segments, digit_to_segments[1]):
                segments_to_digit[current_segments] = 6
            else:
                if not contains(current_segments, digit_to_segments[4]):
                    segments_to_digit[current_segments] = 0
                else:
                    segments_to_digit[current_segments] = 9

    digit_to_segments: Dict[int, List[str]] = dict(
        (value, key) for key, value in segments_to_digit.items()
    )
    # find 2, 3, 5 in third pass
    for value in segments.split(" "):
        if len(value) == nb_segments_by_digit[2]:
            current_segments = "".join(sorted(value))
            if contains(current_segments, digit_to_segments[1]):
                segments_to_digit[current_segments] = 3
            else:
                if contains(digit_to_segments[6], current_segments):
                    segments_to_digit[current_segments] = 5
                else:
                    segments_to_digit[current_segments] = 2

    return segments_to_digit


def decode_output(output: str, segments_to_digit: Dict[str, int]) -> int:
    decoded_output = "".join(
        [
            str(segments_to_digit["".join(sorted(segment))])
            for segment in output.split(" ")
        ]
    )
    return int(decoded_output)


def part_two(content: List[str]):
    total_sum = 0
    for line in content:
        patterns, output = [s.strip() for s in line.split("|")]
        segments_to_digit = derive_segments_to_digit(patterns)
        decoded_output = decode_output(output, segments_to_digit)
        total_sum += decoded_output
    print(total_sum)


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
