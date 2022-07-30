def is_opposite(s1, s2):
    new_s1 = ""
    if len(s1) >= 1 and isinstance(s1, str):
        for items in s1:
            if items.islower():
                new_s1 += items.upper()
            elif items.isupper():
                new_s1 += items.lower()
    print(True) if len(s1) >= 1 and new_s1 == s2 else print(False)
    return True if len(s1) >= 1 and new_s1 == s2 else False


# def is_opposite(s1, s2):
#     return False if not(s1 or s2) else s1.swapcase() == s2


is_opposite("ab", "AB")
# True
is_opposite("aB", "Ab")
# True
is_opposite("aBcd", "AbCD")
# True
is_opposite("AB", "Ab")
# False
is_opposite("", "")
# False