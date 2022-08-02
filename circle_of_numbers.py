# kata 7


def circle_of_numbers(n, fst):
    if n - fst > n / 2:
        print(int(fst + (n / 2)))
    elif n - fst < n / 2:
        print(int(fst - (n / 2)))
    elif n - fst == n / 2:
        print(0)
    else:
        print(int(n/2))


circle_of_numbers(10, 2)
# 7
circle_of_numbers(10, 7)
# 2
circle_of_numbers(4, 1)
# 3
circle_of_numbers(6, 3)
# 0