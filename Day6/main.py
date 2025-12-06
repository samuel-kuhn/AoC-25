import math


def parse_input(filename: str) -> list[str]:
  with open(filename, "r") as f:
    return f.read().splitlines()

def parse_file_to_2d_list(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        num_array = line.split(' ')
        res.append([num for num in num_array if num != ''])
    return res

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



if __name__ == "__main__":
    inp = parse_input("input.txt")
    parsed = parse_file_to_2d_list(inp)
    total = calculate_total(parsed)

    print("Total: ")
    print(total)