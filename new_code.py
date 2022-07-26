def is_vow(inp):
    i = 0
    while i < len(inp):
        if chr(inp[i]) == 'a':
            inp[i] = 'a'
        elif chr(inp[i]) == 'e':
            inp[i] = 'e'
        elif chr(inp[i]) == 'i':
            inp[i] = 'i'
        elif chr(inp[i]) == 'o':
            inp[i] = 'o'
        elif chr(inp[i]) == 'u':
            inp[i] = 'u'
        i += 1
    print(inp)
    return inp


is_vow([101, 121, 110, 113, 113, 103, 121, 121, 101, 107, 103])
