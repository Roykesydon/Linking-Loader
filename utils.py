from typing import List


def hex_to_int(hex_input: str):
    bits = len(hex_input) * 4
    value = int(hex_input, 16)

    if value & (1 << (bits - 1)):
        value -= 1 << bits
    return value


def int_to_hex(input: int, half_bytes: int = None):
    if half_bytes is None:
        half_bytes = len(str(hex(input))[2:]) - (0 if input >= 0 else 1)

    bits = half_bytes * 4

    result = str(hex((input + (1 << bits)) % (1 << bits)))[2:]

    if hex_to_int(result[0]) in range(8, 16):
        result = "F" * (half_bytes - len(result)) + result
    else:
        result = "0" * (half_bytes - len(result)) + result

    return result.upper()


def read_file_lines(filename: str):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]  # remove newline
        return lines


def write_file_lines(lines: List[str], mode: str, output_file_name: str = "output"):
    with open(output_file_name, mode) as f:
        f.write("\n".join(lines))
