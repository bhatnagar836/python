# kata 7
def flatten_and_sort(array):
    new_l = []
    for items in array:
        new_l += items
    new_l.sort()
    print(new_l)
    return new_l


flatten_and_sort([[], [1]])
flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]])