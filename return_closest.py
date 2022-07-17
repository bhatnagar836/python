def closest_multiple_10(i):
    num = i % 10
    return i - num if num < 5 else (i + 10) - num


# def closest_multiple_10(i):
#     print(round(i / 10) * 10)
#     return round(i / 10) * 10


closest_multiple_10(54)
closest_multiple_10(55)