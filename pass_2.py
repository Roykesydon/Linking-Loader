from typing import List

from utils import hex_to_int, int_to_hex, read_file_lines


def pass_2(
    obj_filenames: List[str],
    ESTAB: dict,
    PROGADDR: int,
    virtual_memory_space: List[str],
):
    CSADDR = PROGADDR

    for obj_file_name in obj_filenames:
        lines = read_file_lines(obj_file_name)
        header_record = lines[0]

        CSLTH = hex_to_int(header_record.split()[-1])

        for line in lines[1:]:
            if line[0] == "T":
                record_start = hex_to_int(line[1:7])
                record_length = hex_to_int(line[7:9])

                record_memory_start_index = (CSADDR - PROGADDR + record_start) * 2

                for i in range(record_length * 2):
                    virtual_memory_space[record_memory_start_index + i] = line[9 + i]

            elif line[0] == "M":
                symbol = line[10:]
                record_start = hex_to_int(line[1:7])
                modify_length = hex_to_int(line[7:9])
                operation = line[9]

                if symbol not in ESTAB:
                    raise Exception("undefined external symbol")

                record_memory_start_index = (CSADDR - PROGADDR + record_start) * 2

                if modify_length % 2 == 1:
                    record_memory_start_index += 1

                origin_memory_value = hex_to_int(
                    "".join(
                        virtual_memory_space[
                            record_memory_start_index : record_memory_start_index
                            + modify_length
                        ]
                    )
                )

                origin_memory_value += (
                    ESTAB[symbol] if operation == "+" else -ESTAB[symbol]
                )

                new_memory_value = int_to_hex(origin_memory_value, modify_length)

                for i in range(modify_length):
                    virtual_memory_space[
                        record_memory_start_index + i
                    ] = new_memory_value[i]

        CSADDR += CSLTH

    return CSADDR
