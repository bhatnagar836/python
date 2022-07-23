def solution(digits):
    comparisons = []
    indices = []
    largest = 0
    for items in digits[:len(digits)-4]:
        if int(items) > largest:
            largest = int(items)
    # print(largest)
    current_i = digits.index(str(largest))
    # print("Index: ", current_i)
    count = digits.count(str(largest))
    # print(count)
    if count == 1:
        five_digit_num = digits[int(current_i): int(current_i) + 5]
        print(int(five_digit_num))
        return int(five_digit_num)
    else:
        for i in range(len(digits)-4):
            if str(digits[i]) == str(largest):
                indices.append(i)
        print(indices)
        for i in indices:
            five_digits = digits[int(i): int(i) + 5]
            comparisons.append(int(five_digits))
        print("Largest Number: ", max(comparisons))
        return max(comparisons)


solution('1239456789234765')
solution('1234567898765')




