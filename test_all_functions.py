list_of_numbers_1 = [29, 3, 77, 55]
list_of_numbers_2 = [1.23, 9, 6.97, 7, 27.01]
list_of_numbers_3 = [-7, -8, 26, 54, -2]


def test_sum_list_integer():
    from sumofnumbers import sum_list
    sum_ = sum_list(list_of_numbers_1)
    assert sum_ == 164


def test_sum_list_decimals():
    from sumofnumbers import sum_list
    sum_ = sum_list(list_of_numbers_2)
    assert sum_ == 51.21


def test_sum_list_negative():
    from sumofnumbers import sum_list
    sum_ = sum_list(list_of_numbers_3)
    assert sum_ == 63


def test_min():
    from return_max_min import find_min
    min_ = find_min([4, 7,-20])
    assert min_ == -20


def test_max():
    from return_max_min import find_max
    max_ = find_max([1010, 32 -302931])
    assert max_ == 1010


def test_doubles():
    from return_max_min import find_max
    max_ = find_max([2, 2, 0])
    assert max_ == 2


def test_precision():
    from return_max_min import find_max
    max_ = find_max([1.33, 0, -222])
    assert max_ == 1.33


def test_tuple_size():
    from return_max_min import tuple_generator
    min_max = tuple_generator(23, 53)
    assert len(min_max) == 2