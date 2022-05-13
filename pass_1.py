from typing import List

from utils import hex_to_int, read_file_lines


def pass_1(obj_filenames: List[str], ESTAB: dict, PROGADDR: int):
    CSADDR = PROGADDR

    for obj_file_name in obj_filenames:
        lines = read_file_lines(obj_file_name)
        header_record = lines[0]

        control_section_name = header_record.split()[0][1:]
        CSLTH = hex_to_int(header_record.split()[-1])

        if control_section_name in ESTAB:
            raise Exception("duplicate external symbol")

        ESTAB[control_section_name] = CSADDR

        for line in lines[1:]:
            if line[0] == "D":
                symbols_with_address_list = [
                    line[1 + i : 1 + i + 12] for i in range(0, len(line[1:]), 12)
                ]
                symbols_and_address_list = [
                    (x[:-6].strip(), x[-6:]) for x in symbols_with_address_list
                ]

                for symbol, address in symbols_and_address_list:
                    if symbol in ESTAB:
                        raise Exception("duplicate external symbol")
                    ESTAB[symbol] = hex_to_int(address) + CSADDR

        CSADDR += CSLTH

    return CSADDR - PROGADDR
