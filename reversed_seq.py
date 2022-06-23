def reverse_seq(n):
    new_list = []
    while n > 0:
        new_list.append(n)
        n -= 1
    print(new_list)
    return new_list


reverse_seq(10800000)
