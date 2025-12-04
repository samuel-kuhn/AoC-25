import main as m
grid = m.parse_input("test-input.txt")

assert m.get_accessible_rolls_count(grid) == 13


print("Success")