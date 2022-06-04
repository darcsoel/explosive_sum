from main import exp_sum, exp_sum_recursion


def test1():
    assert exp_sum(1) == 1
    assert exp_sum_recursion(1) == 1


def test2():
    assert exp_sum(2) == 2  # -> 1+1 , 2
    assert exp_sum_recursion(2) == 2  # -> 1+1 , 2


def test3():
    assert exp_sum(3) == 3  # -> 1+1+1, 1+2, 3
    assert exp_sum_recursion(3) == 3  # -> 1+1+1, 1+2, 3


def test4():
    assert exp_sum(4) == 5  # -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
    assert exp_sum_recursion(4) == 5  # -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4


def test5():
    assert exp_sum(5) == 7  # -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3
    assert exp_sum_recursion(5) == 7  # -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3


def test6():
    assert exp_sum(10) == 42
    assert exp_sum_recursion(10) == 42
