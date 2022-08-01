def no_boring_zeros(n):
    if n == 0:
        # print(0)
        return 0
    else:
        while n % 10 == 0:
            n = n / 10
        # print(int(n))
        return int(n)


no_boring_zeros(-960000)