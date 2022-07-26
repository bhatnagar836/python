def merge_arrays(first, second):
    data = list(set(first + second))
    data.sort()
    print(data)
    return data


merge_arrays([1, 3, 3, 5], [2, 4, 6])
