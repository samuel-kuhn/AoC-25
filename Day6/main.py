import math
from itertools import zip_longest


def parse_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def parse_file_to_2d_list(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        num_array = line.split(' ')
        res.append([num for num in num_array if num != ''])
    return res


def parse_file_to_2d_list_filled_vertically(lines: list[str]) -> tuple[list[list[int]], list[str]]:
    res: list[list[int]] = []
    ops = [op for op in lines.pop().split(' ') if op != '']
    num_stack = []

    max_len = max(len(line) for line in lines)
    padded = [line.ljust(max_len) for line in lines] # ljust pads each line with spaces to match max_len

    for column_index in range(max_len):
        num_str = ""
        for row in padded:
            num_str += row[column_index]
        if not num_str.isspace():
            num_stack.append(int(num_str))
        else:
            res.append(num_stack)
            num_stack = []

    res.append(num_stack)
    return res, ops


def calculate_total(num_2d_list: list[list[str]]) -> int:
    total = 0
    ops = num_2d_list.pop()
    inverted = [[row[i] for row in num_2d_list] for i in range(len(num_2d_list[0]))]
    for row in inverted:
        op = ops.pop(0)
        if op == '*':
            total += math.prod([int(i) for i in row])
        elif op == '+':
            total += sum([int(i) for i in row])
        else:
            raise Exception(f"Unknown operator: {op}")
    return total


def calculate_total_right_to_left(num_2d_list: list[list[int]], ops: list[str]) -> int:
    total = 0

    for row in num_2d_list:
        op = ops.pop(0)
        if op == '*':
            total += math.prod(row)
        elif op == '+':
            total += sum(row)
        else:
            raise Exception(f"Unknown operator: {op}")
    return total


if __name__ == "__main__":
    inp = parse_input("input.txt")
    parsed = parse_file_to_2d_list(inp)
    total = calculate_total(parsed)

    print("Total M1: ")
    print(total)

    parsed_nums, ops = parse_file_to_2d_list_filled_vertically(inp)
    total_m2 = calculate_total_right_to_left(parsed_nums, ops)
    print("Total M2:")
    print(total_m2)
