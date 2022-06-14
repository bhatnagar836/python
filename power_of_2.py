def powers_of_two(n):
    new_list = []
    while n >= 0:
        number = 2**n
        new_list.append(number)
        n -= 1
    new_list.sort()
    print(new_list)
    return new_list


powers_of_two(2)

