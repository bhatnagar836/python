def stringy(size):
    string = ""
    for items in range(int(size / 2)):
        string = string + '10'
    # print(string)
    if size % 2:
        string = string + '1'

    print(string)
    return string

# def stringy(size):
#     return '10' * (size // 2) + '1' * (size % 2)


stringy(17)
