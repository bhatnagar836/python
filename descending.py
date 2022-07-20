def descending_order(num):
    new_list = []
    for items in str(num):
        new_list.append(items)
    new_list.sort(reverse=True)
    print(new_list)
    print("".join(new_list))
    return int("".join(new_list))


# def Descending_Order(num):
#     return int("".join(sorted(str(num), reverse=True)))

descending_order(145263)
