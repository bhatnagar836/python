def divisible_by(numbers, divisor):
    new_l = []
    for items in numbers:
        if items%divisor == 0:
            new_l.append(items)
        else:
            pass
    return new_l
