def product_array(numbers):
    result = 1
    new_list = []
    for items in numbers:
        result = (result * items)
    for i in range(len(numbers)):
        new_list.append(int(result/numbers[i]))
    # print(new_list)
    return new_list


product_array([16, 17, 4, 3, 5, 2])