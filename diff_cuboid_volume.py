def find_difference(a, b):
    def cuboid_vol(arr):
        result = 1
        for each_ele in arr:
            result *= each_ele
        return result
    vol_1 = cuboid_vol(a)
    vol_2 = cuboid_vol(b)
    if vol_2 > vol_1:
        print(vol_2-vol_1)
        return vol_2-vol_1
    else:
        print(vol_1-vol_2)
        return vol_1-vol_2


# from numpy import prod
#
# def find_difference(a, b):
#     return abs(prod(a) - prod(b))


find_difference([3, 2, 5], [1, 4, 4])
find_difference([9, 7, 2], [5, 2, 2])

