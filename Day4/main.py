def parse_input(filename: str) -> list[str]:
  with open(filename, "r") as f:
    return f.read().splitlines()


def is_accessible_roll(grid: list[str], x: int, y:int) -> int:
    """
    assuming grid[x][y] is a roll
    :return: True if roll has less then 4 adjacent rolls
    """
    rolls_count = 0
    grid_width = len(grid[0])
    grid_height = len(grid)
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y: # middle of 3x3 field
                continue
            if i < 0 or j < 0: # outside of grid
                continue
            if i >= grid_width or j >= grid_height: # outside of grid
                continue

            if grid[i][j] == '@':
                rolls_count += 1

    return rolls_count < 4

def get_accessible_rolls_count(grid: list[str]):
    accessible_rolls = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[x][y] == '@' and is_accessible_roll(grid, x, y):
                accessible_rolls += 1
    return accessible_rolls

if __name__ == "__main__":
    grid = parse_input("input.txt")
    print(get_accessible_rolls_count(grid))