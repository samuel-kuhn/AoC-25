import builtins


def parse_input(filename:str) -> list[str]:
    with open(filename, "r") as f:
        id_range_full_string = f.readline()
    id_range_strings = id_range_full_string.split(',')
    return id_range_strings

def calculate_invalid_ids_per_range_m1(id_range: str) -> list[int]:
    invalid_ids = []

    range_split = id_range.split('-')
    start = int(range_split[0])
    end = int(range_split[1]) + 1
    for num in range(start, end):
        num_string = str(num)
        num_length = len(num_string)
        if num_length % 2 == 0:
            half_length = int(num_length/2)
            first_half = num_string[:half_length]
            if first_half * 2 == num_string:
                invalid_ids.append(num)

    return invalid_ids

def calculate_invalid_ids_per_range_m2(id_range: str) -> list[int]:
    invalid_ids = []

    range_split = id_range.split('-')
    start = int(range_split[0])
    end = int(range_split[1]) + 1
    for num in range(start, end):
        num_string = str(num)
        num_length = len(num_string)

        for sequence_length in range(1,int(num_length/2)+1):
            if num_length % sequence_length == 0:
                sequence = num_string[:sequence_length]
                if sequence * int(num_length/sequence_length) == num_string:
                    invalid_ids.append(num)

    return invalid_ids

def calculate_invalid_id_sum(invalid_id_list: list[str], method) -> int:
    invalid_ids: list[int] = []
    res = 0
    for id_range in invalid_id_list:
        invalid_ids += method(id_range)

    for invalid_id in set(invalid_ids): # set to avoid duplicate entries
        res += invalid_id
    return res


if __name__ == "__main__":
    result1 = calculate_invalid_id_sum(parse_input("input.txt"), calculate_invalid_ids_per_range_m1)
    print("Result 1: " + str(result1))
    result2 = calculate_invalid_id_sum(parse_input("input.txt"), calculate_invalid_ids_per_range_m2)
    print("Result 2: " + str(result2))
