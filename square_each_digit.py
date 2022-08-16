# def square_digits(num):
#     if num == 0:
#         return 0
#     else:
#         new_list = []
#         while num >= 1:
#             rem = num % 10
#             new_list.append(str(rem ** 2))
#             num = int((num - rem) / 10)
#         new_list.reverse()
#         # print(new_list)
#         # print("".join(new_list))
#         return int("".join(new_list))


# square_digits(9112)

def binary_array_to_number(arr):
    new_s = ""
    for items in arr:
        new_s += str(items)
    binary_num = int(new_s,2)
    print(binary_num)
    return binary_num




binary_array_to_number([0,0,0,1])