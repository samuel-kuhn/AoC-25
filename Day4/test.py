import main as m
m.grid = m.parse_input("test-input.txt")

assert m.get_accessible_rolls_count_m1() == 13
assert m.get_total_accessible_rolls_count() == 43

print("Success")