def sum_of_differences(arr):
    new_list = []
    array = sorted(arr, reverse=True)
    print(array)
    for i in range(len(array) - 1):
        current_item = array[i]
        # print(current_item)
        next_item = array[i + 1]
        # print(next_item)
        difference = current_item - next_item
        new_list.append(difference)
    # print(new_list)
    total = sum(new_list)
    # print(total)
    return total

# def sum_of_differences(arr):
#     arr.sort(reverse=True)
#     i = 0
#     res = 0
#     while i < len(arr)-1:
#         res += arr[i] - arr[i+1]
#         i += 1
#     print(res)
#     return res


sum_of_differences([1, 5, 2, 10])
