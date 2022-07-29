def feast(beast, dish):
    b_first = beast[0]
    b_last = beast[len(beast)-1]
    d_first = dish[0]
    d_last = dish[len(dish)-1]
    return True if b_first == d_first and b_last == d_last else False


# def feast(beast, dish):
#     return beast[0] == dish[0] and dish[-1] == beast[-1]


feast("great blue heron", "garlic naan")
feast("chickadee", "chocolate cake")
feast("brown bear", "bear claw")
