# kata 7
def div_con(x):
    non_string_sum = 0
    string_sum = 0
    for items in x:
        if isinstance(items, int):
            non_string_sum += items
            # print("Non String Sum :", non_string_sum)
        elif isinstance(items, str):
            string_sum += int(items)
            # print("String Sum :", string_sum)
    print(non_string_sum - string_sum)
    return non_string_sum - string_sum


# def div_con(lst):
#     print(sum(n if isinstance(n, int) else -int(n) for n in lst))
#     return sum(n if isinstance(n, int) else -int(n) for n in lst)

div_con([9, 3, '7', '3'])
# 2
div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7])
# 14
div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'])
# 13
div_con(['1', '5', '8', 8, 9, 9, 2, '3'])
# 11
div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7])
# 61