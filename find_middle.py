# kata7
def gimme(input_array):
    print(input_array)
    largest = max(input_array)
    smallest = min(input_array)
    for item in input_array:
        if item == largest:
            pass
        elif item == smallest:
            pass
        else:
            middle_ele = item
    print(input_array.index(middle_ele))
    return input_array.index(middle_ele)


# def gimme(inputArray):
#     return inputArray.index(sorted(inputArray)[1])

gimme([1, 5, 14])
gimme([-74, -73, -87])