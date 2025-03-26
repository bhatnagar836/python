# Map, Filter, Reduce - can help in performance improvement


# ********************************************MAP******************************************************
# Map Function - return map object
# To perform a function on every element of the list:

numbers = ["3", "21", "11"]

"""
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print(numbers)
"""
# Above can be done in one line without for loop

numbers = list(map(int, numbers))
# Above - int function is used to typecast all the elements to integer and return the map object typecasted to list
print(numbers)


def sq(a):
    return a*a
# Instead of giving the name of the function, we can also use lambda


# numbers = list(map(sq, numbers))
numbers = list(map(lambda x: x*x, numbers))
print(numbers)


def sq_is(a):
    return a*a

def cube_is(b):
    return b*b*b

funct = [sq_is, cube_is]

for i in range(1, 6):
    numbers_ = list(map(lambda x: x(i), funct))
    # Here in lambda we are stating that if we are giving a function "x" then it will return the function of i
    # Example if function name is square, then it will return square of i (which starts with 1 here) and list is "funct"
    # Giving output like sq(3) = 9, cube(3) = 27 applied on funct gives [9, 27]
    print(numbers_)


# ********************************************FILTER******************************************************

list2 = [11, 21, 3, 4, 5, 61, 71, 8, 9]
def is_greater_5(num):
    return num > 5


# Filter is used to filter over an iterable object on the basis of some functions
gr_than_5 = list(filter(is_greater_5, list2))
print(gr_than_5)

# ********************************************REDUCE******************************************************
# Reduce is part of functool module
from functools import reduce

# Example: we need an operation to form on list (adding all elements of the list)

sum = 0
list3 = [1, 3, 5, 7, 9]
for i in list3:
    sum = sum + i
# print(sum)


# Or, we can do it as follows (using reduce) which will perform operation (or function) mentioned on every consecutive numbers of the list
# E.g. First 1+3= 4, then 4+5 = 9, then 9+7 = 16

sum1 = reduce((lambda a,b: a+b), list3)
print(sum1)


