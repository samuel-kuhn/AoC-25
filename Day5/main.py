def parse_input(filename: str) -> list[str]:
  with open(filename, "r") as f:
    return f.read().splitlines()


def parse_id_range(id_range: str) -> tuple:
    range_split = id_range.split('-')
    return tuple([int(i) for i in range_split])

def get_all_id_ranges(id_ranges_strings: list[str]) -> list[tuple]:
    tuple_list = []
    for id_range_string in id_ranges_strings:
        tuple_list.append(parse_id_range(id_range_string))

    return tuple_list

def is_valid_id(ingredient_id: int, tuple_list: list[tuple]) -> bool:
    for t in tuple_list:
        if t[0] <= ingredient_id <= t[1]:
            return True
    return False

def get_valid_id_count(id_list: list[int], tuple_list: list[tuple]) -> int:
    return sum(is_valid_id(i, tuple_list) for i in id_list) # sum adds 1 for True and 0 for False for each i in id_list

def get_total_fresh_ingredient_ids(tuple_list: list[tuple]) -> int:
    count = 0
    for t in tuple_list:
        count += t[1] - t[0] + 1 # + 1 because first and last also counts
    return count

def sort_and_merge_tuple_list(tuple_list: list[tuple]) -> list[tuple]:
    tuple_list.sort()
    unmerged_list = tuple_list
    merged_list = []
    t = unmerged_list.pop(0)
    for t_next in unmerged_list:
        t_merged = merge_or_return_none(t, t_next)
        if t_merged:
            t = t_merged
        else:
            merged_list.append(t)
            t = t_next
    merged_list.append(t_next)
    return merged_list



def merge_or_return_none(t: tuple, t_next: tuple) -> tuple | None:
    if t_next[0] <= t[1]:
        return t[0], max(t[1], t_next[1])
    return None

if __name__ == "__main__":
    id_ranges = parse_input("id_ranges.txt")
    id_range_tuples = get_all_id_ranges(id_ranges)
    id_list = parse_input("input.txt")
    id_list = [int(i) for i in id_list]
    fresh_ingredients = get_valid_id_count(id_list, id_range_tuples)

    merged_list = sort_and_merge_tuple_list(id_range_tuples)
    total_count = get_total_fresh_ingredient_ids(merged_list)

    print("Fresh Ingredients:")
    print(fresh_ingredients)

    print("Total id count:")
    print(total_count)

