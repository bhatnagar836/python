import math


def collatz(n):
    new_l = [n]
    while n > 1:
        if n % 2 == 0:
            n = math.floor(n/2)
            print(n)
            new_l.append(n)
        elif n % 2 != 0:
            n = math.floor((n*3)+1)
            print(n)
            new_l.append(n)
    # print(new_l)
    # print(len(new_l))
    return len(new_l)


collatz(220702396557840715720)
