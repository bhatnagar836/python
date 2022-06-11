# To square(root) or not to square(root)
# 8 kyu
import math


def square_or_square_root(arr):
    new_list = []
    for item in arr:
        if math.ceil(math.sqrt(item)) == math.floor(math.sqrt(item)):
            square_root = math.sqrt(item)
            new_list.append(int(square_root))
        else:
            square = int(pow(item, 2))
            new_list.append(square)
    print(new_list)
    return new_list


square_or_square_root([4, 2, 3, 9, 100, 101])

# Example of optimal solution
def square_or_square_root(arr):
    return [i**0.5 if (i**0.5).is_integer() else i**2 for i in arr]