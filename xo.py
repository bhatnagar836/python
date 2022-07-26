def xo(s):
    count1 = 0
    count2 = 0
    for char in s:
        if char == 'o' or char == 'O':
            count1 += 1
        elif char == 'x' or char == 'X':
            count2 += 1
        else:
            pass
    print(count1, count2)
    print(True) if count1 == count2 else print(False)
    return True if count1 == count2 else False


xo("ooxXm")