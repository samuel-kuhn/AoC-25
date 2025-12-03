from operator import index


def parse_input(filename: str) -> list[str]:
  with open(filename, "r") as f:
    return f.read().splitlines()

def get_largest_joltage(bank: str) -> int:
  int_list = [int(char) for char in bank]
  first_digit = max(int_list[:-1]) # biggest digit except for the last digit
  i_first_digit = int_list.index(first_digit)
  second_digit = max(int_list[i_first_digit+1:])
  return int(str(first_digit)+str(second_digit))


def get_largest_joltage_p2(bank: str) -> int:
  int_list = [int(char) for char in bank]
  biggest_joltage_string = ""
  for i in range(1,13): # 1 to 12
    n = 12 - i
    if not n == 0:
      current_max_digit = max(int_list[:-n]) # biggest digit except for the last n digits
    else:
      current_max_digit = max(int_list)
    biggest_joltage_string += str(current_max_digit)

    entries_to_remove = 1 + int_list.index(current_max_digit)
    int_list = int_list[entries_to_remove:] # make sure the next digit comes after the current max digit

  return int(biggest_joltage_string)

def get_total_joltage(banks: list[str], method) -> int:
  return sum([method(bank) for bank in banks])

if __name__ == "__main__":
  print(get_total_joltage(parse_input("input.txt"), get_largest_joltage))
  print(get_total_joltage(parse_input("input.txt"), get_largest_joltage_p2))



