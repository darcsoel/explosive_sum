def exp_sum_recursion(number: int, lower_bound=1) -> int:
    if lower_bound > number:
        return 0
    elif lower_bound == number:
        return 1
    else:
        return exp_sum_recursion(number - lower_bound, lower_bound) + exp_sum_recursion(number, lower_bound + 1)


def exp_sum(number: int) -> int:
    sum_list = [1 for _ in range(number+1)]

    for i in range(1, number+1):
        for j in range(i, number+1):
            sum_list[j] += sum_list[j-i]

    return sum_list[number] - sum_list[number-1]
