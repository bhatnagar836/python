def multi_table(number):
    new_list = []
    for num in range(1, 10):
        multi = f"{num} * {number} = {num * number}\n"
        new_list.append(multi)
    for num in range(10, 11):
        multi = f"{num} * {number} = {num * number}"
        new_list.append(multi)
    # print(new_list)
    return "".join(new_list)


multi_table(5)
