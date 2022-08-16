def square_digits(num):
    if num == 0:
        return 0
    else:
        new_list = []
        while num >= 1:
            rem = num % 10
            new_list.append(str(rem ** 2))
            num = int((num - rem) / 10)
        new_list.reverse()
        # print(new_list)
        # print("".join(new_list))
        return int("".join(new_list))


square_digits(9112)
