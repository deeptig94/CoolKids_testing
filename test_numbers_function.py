from numbers_function import NumbersFunction


def test_sum_list():
    a = NumbersFunction([6, 7, 8])
    assert a.sum_list() == 21


def test_find_min_max():
    b = NumbersFunction([1, 2, 3])
    assert b.find_min_max() == 1 & 3


def test_max_diff():
    c = NumbersFunction([4, 5, 6])
    assert c.max_diff() == 2
