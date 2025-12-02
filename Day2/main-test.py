import gift_shop as g

parsed_file = g.parse_input("test-input.txt")

def test_parse_input():
        output = parsed_file
        assert output[0] == "11-22"
        assert output[10] == "2121212118-2121212124"

def test_calculate_invalid_ids_per_range_m1():
    range_list = parsed_file
    assert g.calculate_invalid_ids_per_range_m1(range_list[0]) == [11, 22]
    assert g.calculate_invalid_ids_per_range_m1("38593856-38593862") == [38593859]

def test_calculate_invalid_id_sum_m1():
    res = g.calculate_invalid_id_sum(parsed_file, g.calculate_invalid_ids_per_range_m1)
    assert res == 1227775554

def test_puzzle_answer():
    parsed_input = g.parse_input("input.txt")
    assert g.calculate_invalid_id_sum(parsed_input, g.calculate_invalid_ids_per_range_m1) == 31839939622

### Part 2

def test_calculate_invalid_ids_per_range_m2():
    assert g.calculate_invalid_ids_per_range_m2(parsed_file[0]) == [11, 22]
    assert g.calculate_invalid_ids_per_range_m2(parsed_file[1]) == [99, 111]
    assert g.calculate_invalid_ids_per_range_m2("446443-446449") == [446446]
    assert g.calculate_invalid_ids_per_range_m2("998-1012") == [999, 1010]
    assert g.calculate_invalid_ids_per_range_m2("824824821-824824827") == [824824824]
    assert g.calculate_invalid_ids_per_range_m2("2121212118-2121212124") == [2121212121]



def test_calculate_invalid_id_sum_m2():
    res = g.calculate_invalid_id_sum(parsed_file, g.calculate_invalid_ids_per_range_m2)
    assert res == 4174379265


if __name__ == '__main__':
    test_parse_input()
    test_calculate_invalid_ids_per_range_m1()
    test_calculate_invalid_id_sum_m1()
    test_puzzle_answer()
    # Part 2
    test_calculate_invalid_ids_per_range_m2()
    test_calculate_invalid_id_sum_m2()
    print("Success!")
