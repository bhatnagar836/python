def high_and_low(numbers):
    a = numbers.split()
    ints = []
    for element in a:
        ints.append(int(element))

    highest = str(max(ints))
    lowest = str(min(ints))
    print(highest + " " + lowest)
    return highest + " " + lowest


# def high_and_low(numbers):
#     numbers = [int(x) for x in numbers.split(" ")]
#     return str(max(numbers)) + " " + str(min(numbers))


# high_and_low("1 2 -3 4 5")
high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")