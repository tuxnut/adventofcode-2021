import os
import sys
from typing import Dict, List


def read_input_file(filename: str) -> List[str]:
    content = []
    with open(filename) as f:
        content = [line for line in f]

    return content


def retrieve_most_common_bit_in_every_position(
    binary_numbers: List[str],
) -> Dict[int, int]:
    number_of_bit_0_in_every_position = {}
    for number in binary_numbers:
        for position, bit in enumerate(number):
            if bit == "0" or bit == "1":
                if position not in number_of_bit_0_in_every_position:
                    number_of_bit_0_in_every_position[position] = 1
                else:
                    number_of_bit_0_in_every_position[position] += (
                        1 if bit == "0" else 0
                    )

    half_content = len(binary_numbers) / 2
    most_common_bit_for_every_position = {}
    for position, number_of_0 in number_of_bit_0_in_every_position.items():
        most_common_bit_for_every_position[position] = (
            0 if number_of_0 > half_content else 1
        )

    return most_common_bit_for_every_position


def convert_most_common_bits_to_gamma_rate(most_common_bits: Dict[int, int]) -> int:
    gamma_rate_b = ""
    for bit in most_common_bits.values():
        gamma_rate_b += str(bit)

    gamma_rate = int(gamma_rate_b, 2)
    print(f"The gamma rate is {gamma_rate_b}={gamma_rate}")
    return gamma_rate


def convert_most_common_bits_to_epsilon_rate(most_common_bits: Dict[int, int]) -> int:
    epsilon_rate_b = ""
    for bit in most_common_bits.values():
        opposite_bit = 1 if bit == 0 else 0
        epsilon_rate_b += str(opposite_bit)

    epsilon_rate = int(epsilon_rate_b, 2)
    print(f"The epsilon rate is {epsilon_rate_b}={epsilon_rate}")
    return epsilon_rate


def retrieve_most_common_bit_in_position(
    binary_numbers: List[str], position: int
) -> int:
    count_of_number_with_bit_0_at_pos = 0
    for number in binary_numbers:
        if number[position] == "0":
            count_of_number_with_bit_0_at_pos += 1

    half_content = len(binary_numbers) / 2
    return 0 if count_of_number_with_bit_0_at_pos > half_content else 1


def filter_out_number(binary_numbers: List[str], position: int, bit: str) -> List[str]:
    return [number for number in binary_numbers if number[position] == bit]


def find_oxygen_generator_rating(binary_numbers: List[str]) -> int:
    searching = True
    position = 0
    while searching and position < len(binary_numbers[0]):
        most_common_bit_in_position = retrieve_most_common_bit_in_position(
            binary_numbers, position
        )
        binary_numbers = filter_out_number(
            binary_numbers, position, str(most_common_bit_in_position)
        )
        if len(binary_numbers) == 1:
            searching = False
            oxygen_generator_rating = int(binary_numbers[0], 2)
            print(
                f"The oxygen generator rating is {binary_numbers[0]}={oxygen_generator_rating}"
            )
            return oxygen_generator_rating
        position += 1


def find_co2_scrubber_rating(binary_numbers: List[str]) -> int:
    searching = True
    position = 0
    while searching and position < len(binary_numbers[0]):
        most_common_bit_in_position = retrieve_most_common_bit_in_position(
            binary_numbers, position
        )
        opposite_bit = 1 if most_common_bit_in_position == 0 else 0
        binary_numbers = filter_out_number(binary_numbers, position, str(opposite_bit))
        if len(binary_numbers) == 1:
            searching = False
            co2_scrubber_rating = int(binary_numbers[0], 2)
            print(
                f"The CO2 scrubber rating is {binary_numbers[0]}={co2_scrubber_rating}"
            )
            return co2_scrubber_rating
        position += 1


def main(argv: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input_file(f"{current_dir}/input.txt")

    if argv == "1":
        most_common_bits = retrieve_most_common_bit_in_every_position(content)
        gamma_rate = convert_most_common_bits_to_gamma_rate(most_common_bits)
        epsilon_rate = convert_most_common_bits_to_epsilon_rate(most_common_bits)
        print(
            f"The power consumption is [{gamma_rate=}, {epsilon_rate=}] -> {gamma_rate * epsilon_rate}"
        )
    elif argv == "2":
        most_common_bits = retrieve_most_common_bit_in_every_position(content)
        oxygen_generator_rating = find_oxygen_generator_rating(content.copy())
        co2_scrubber_rating = find_co2_scrubber_rating(content.copy())
        print(
            f"The life support rating is [{oxygen_generator_rating=}, {co2_scrubber_rating=}] -> {oxygen_generator_rating * co2_scrubber_rating}"
        )
    else:
        print("Expected argument: '1' for part_one or '2' for part_two")


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
