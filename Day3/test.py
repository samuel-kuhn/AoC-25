import main as m

banks = m.parse_input("test-input.txt")
assert sum([m.get_largest_joltage(bank) for bank in banks]) == 357

### Part 2

expected_joltage_list = [987654321111,811111111119,434234234278,888911112111]
for i in range(4):
  expected = expected_joltage_list[i]
  actual = m.get_largest_joltage_p2(banks[i])
  assert actual == expected


print("Success")
