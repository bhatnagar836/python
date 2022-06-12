def square_sum(arr):
    sum = 0
    new_list = [x**2 for x in arr]
    for num in new_list:
        sum = sum + num
    # print(sum)
    return sum

# def square_sum(numbers):
#     print(sum(x ** 2 for x in numbers))
#     return sum(x ** 2 for x in numbers)


square_sum([1, 2, 2])
square_sum([1,2])
square_sum([0, 3, 4, 5])
