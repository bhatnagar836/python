def shortcut(s):
    new_s = ""
    for items in s:
        if items == 'a' or items == 'e' or items == 'i' or items == 'o' or items == 'u':
            pass
        else:
            new_s += items
    print(new_s)
    return new_s


# def shortcut(s):
#     return ''.join(c for c in s if c not in 'aeiou')


shortcut('hello')
