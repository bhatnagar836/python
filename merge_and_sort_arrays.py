import numpy as np


def merge_arrays(arr1, arr2):
    con = np.concatenate((arr1, arr2))
    con.sort()
    # print(con)
    result = []
    for i in con:
        if i not in result:
            result.append(i)
    print(result)
    return result


merge_arrays([1,3,5,7,9,11,12], [1,2,3,4,5,10,12])