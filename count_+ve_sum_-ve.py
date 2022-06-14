def count_positives_sum_negatives(arr):
    count = 0
    sum_of = 0
    new_arr = []
    for item in arr:
        if item > 0:
            count += 1
        elif item < 0:
            sum_of = sum_of + item
        else:
            pass
        new_arr = [count, sum_of]
    print(new_arr)
    return new_arr


count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])

