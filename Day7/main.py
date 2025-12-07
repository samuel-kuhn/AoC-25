def parse_input(filename: str) -> list[list[str]]:
    with open(filename, "r") as f:
        return [list(line) for line in f.read().splitlines()]


diagram: list[list[str]] = []
ROW_COUNT = 0
COLUMN_COUNT = 0


def get_starting_point() -> tuple[int, int]:
    return 0, diagram[0].index('S')


def draw_beam() -> int:
    count = 0
    grid = diagram
    for row in range(2, len(grid)):
        for column in range(len(grid[0])):
            field = grid[row][column]
            field_above = grid[row - 1][column]
            if field_above == '|':
                if field == '.':
                    grid[row][column] = '|'
                elif field == '^':
                    count += 1
                    grid[row][column - 1] = '|'
                    grid[row][column + 1] = '|'

    for line in grid:
        print(''.join(line))
    return count


from functools import lru_cache
@lru_cache(None)
# caches outputs of a method so if it is called again with the same parameters it does not need to run again
def count_timelines(row: int, column: int) -> int:
    if row == ROW_COUNT - 1 or column == COLUMN_COUNT - 1:
        return 1

    field = diagram[row][column]
    if field == '.' or field == '|':
        return count_timelines(row + 1, column)
    elif field == '^':
        return count_timelines(row, column - 1) + count_timelines(row, column + 1)
    else:
        raise Exception(f"unkown field: ${field}")


if __name__ == "__main__":
    diagram = parse_input("input.txt")
    ROW_COUNT = len(diagram)
    COLUMN_COUNT = len(diagram[0])

    s_point = get_starting_point()
    s_row, s_column = s_point
    diagram[s_row + 1][s_column] = '|'
    split_count = draw_beam()

    print("Split count:")
    print(split_count)

    timeline_count = count_timelines(s_row + 1, s_column)
    print(timeline_count)
