def first_non_consecutive(arr):
    first = arr[0]
    if not arr or len(arr) == 1:
        return None
    elif len(arr) >= 2:
        for i in range(len(arr)-1):
            current_item = arr[i]
            # print(current_item)
            next_item = arr[i+1]
            # print(next_item)
            if current_item != next_item - 1:
                print(next_item)
                return next_item
        else:
            print(None)
            return None


# def first_non_consecutive(arr):
#     if not arr: return 0
#     for i, x in enumerate(arr[:-1]):
#         if x + 1 != arr[i + 1]:
#             print(arr[i + 1])
#             return arr[i + 1]


first_non_consecutive([1, 2, 3, 4, 6, 7, 8])


