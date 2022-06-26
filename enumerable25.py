def take(arr, n):
    new_list = []
    if not arr :
        return new_list
    elif arr and n <= len(arr):
        for i in range(0, n):
            new_list.append(arr[i])
        print(new_list)
        return new_list
    else:
        return arr


take([0, 1, 2, 3, 5, 8, 13], 3)