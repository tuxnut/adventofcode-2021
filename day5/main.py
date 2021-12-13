import os
import sys
from typing import List, NamedTuple

Point = NamedTuple("Point", [("x", int), ("y", int)])
Segment = NamedTuple("Segment", [("start", Point), ("end", Point)])


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


def parse_points(point_str: str) -> Point:
    x, y = point_str.split(",")
    return Point(int(x), int(y))


def create_segments_from_input(input_list: List[str]) -> List[Segment]:
    segments = []
    for line in input_list:
        parsed_line = line.split("->")
        start_point = parse_points(parsed_line[0])
        end_point = parse_points(parsed_line[1])
        segment = Segment(start_point, end_point)
        segments.append(segment)

    return segments


def is_segment_straight(segment: Segment) -> bool:
    return segment.start.x == segment.end.x or segment.start.y == segment.end.y


def write_straight_segment_to_diagram(
    segment: Segment, diagram: List[List[int]]
) -> None:
    start_x = min(segment.start.x, segment.end.x)
    end_x = max(segment.start.x, segment.end.x)
    start_y = min(segment.start.y, segment.end.y)
    end_y = max(segment.start.y, segment.end.y)
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            diagram[x][y] += 1


def write_diagonal_segment_to_diagram(
    segment: Segment, diagram: List[List[int]]
) -> None:
    length = abs(segment.start.x - segment.end.x)
    x_direction = 1 if segment.start.x < segment.end.x else -1
    y_direction = 1 if segment.start.y < segment.end.y else -1
    for i in range(length + 1):
        x = segment.start.x + (i * x_direction)
        y = segment.start.y + (i * y_direction)
        diagram[x][y] += 1


def build_diagram(segments: List[Segment], with_diagonal: bool) -> List[List[int]]:
    diagram = [[0 for i in range(1000)] for j in range(1000)]
    for segment in segments:
        if is_segment_straight(segment):
            write_straight_segment_to_diagram(segment, diagram)
        elif with_diagonal:
            write_diagonal_segment_to_diagram(segment, diagram)

    return diagram


def count_overlapping_points(diagram: List[List[int]]) -> int:
    count = 0
    for row in diagram:
        for cell in row:
            if cell >= 2:
                count += 1

    return count


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        segments = create_segments_from_input(content)
        diagram = build_diagram(segments, with_diagonal=False)
        overlapping_points = count_overlapping_points(diagram)
        print(f"Overlapping points: {overlapping_points}")
    elif argv == "2":
        segments = create_segments_from_input(content)
        diagram = build_diagram(segments, with_diagonal=True)
        overlapping_points = count_overlapping_points(diagram)
        print(f"Overlapping points: {overlapping_points}")
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
