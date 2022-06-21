def digitize(n):
    n = str(n)
    new_list = []
    for each_item in n:
        new_list.append(int(each_item))
    # print(new_list)
    new_list.reverse()
    print(new_list)
    return new_list


digitize(35231)
digitize(0)