def switcheroo(s):
    new_l = []
    for char in s:
        new_l.append(char)
    print(new_l)
    i = 0
    while i < len(new_l):
        if new_l[i] == 'a':
            new_l[i] = 'b'
        elif new_l[i] == 'b':
            new_l[i] = 'a'
        else:
            new_l[i] = new_l[i]
        i += 1
    # print("".join(new_l))
    return "".join(new_l)


switcheroo("abc")