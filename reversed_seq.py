def reverse_seq(n):
    new_list = []
    while n > 0:
        new_list.append(n)
        n -= 1
    print(new_list)
    return new_list

# def reverse_seq(n):
#     return list(range(n, 0, -1))


reverse_seq(108)
