def parse_input(filename: str) -> list[list[str]]:
    with open(filename, "r") as f:
        return [list(line.rstrip()) for line in f]


grid = [[]]


def is_accessible_roll(x: int, y: int) -> int:
    """
    assuming grid[x][y] is a roll
    :return: True if roll has less then 4 adjacent rolls
    """
    rolls_count = 0
    grid_width = len(grid[0])
    grid_height = len(grid)
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:  # middle of 3x3 field
                continue
            if i < 0 or j < 0:  # outside of grid
                continue
            if i >= grid_width or j >= grid_height:  # outside of grid
                continue

            if grid[i][j] == '@':
                rolls_count += 1

    return rolls_count < 4


def get_accessible_rolls_count_m1():
    accessible_rolls = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[x][y] == '@' and is_accessible_roll(x, y):
                accessible_rolls += 1
    return accessible_rolls


def get_accessible_rolls_count():
    global grid
    grid_copy = grid
    accessible_rolls = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[x][y] == '@' and is_accessible_roll(x, y):  # do not touch original grid and remove in copy
                accessible_rolls += 1
                grid_copy[x][y] = '.'
    grid = grid_copy
    return accessible_rolls


def get_total_accessible_rolls_count():
    total_accessible_rolls = 0
    while True:
        accessible_rolls = get_accessible_rolls_count()
        if accessible_rolls == 0:
            break
        else:
            total_accessible_rolls += accessible_rolls
    return total_accessible_rolls


if __name__ == "__main__":
    grid = parse_input("input.txt")
    print("First process:")
    print(get_accessible_rolls_count_m1())

    print("Total process:")
    print(get_total_accessible_rolls_count())
