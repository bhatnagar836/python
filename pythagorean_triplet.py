def pythagorean_triple(integers):
    integers.sort()
    if integers[2] > integers[0] and integers[2] > integers[1]:
        sum_of_ints = (integers[0]**2) + (integers[1]**2)
        square_of_int = (integers[2]**2)
        return True if sum_of_ints == square_of_int else False
    else:
        return False

pythagorean_triple([3, 4, 5])