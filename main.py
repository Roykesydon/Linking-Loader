import sys

from pass_1 import pass_1
from pass_2 import pass_2
from utils import hex_to_int, int_to_hex, write_file_lines

PROGADDR = hex_to_int(sys.argv[1])
ESTAB = {}

obj_filenames = sys.argv[2:]

total_program_size = pass_1(obj_filenames, ESTAB, PROGADDR)

"""
Wrtie ESTAB
"""
lines = []
for key, value in ESTAB.items():
    line = key + ":0x" + int_to_hex(value, 4).lower()
    lines.append(line)
lines.append("\n")
write_file_lines(lines, "w")

virtual_memory_space = ["."] * (total_program_size * 2)


pass_2(obj_filenames, ESTAB, PROGADDR, virtual_memory_space)

"""
Write memory
"""
lines = []
for i in range((len(virtual_memory_space) + 31) // 32):
    index_start = i * 32
    line = int_to_hex(index_start // 2 + PROGADDR) + " "
    line += " ".join(virtual_memory_space[index_start : index_start + 32])
    lines.append(line)
write_file_lines(lines, "a")
