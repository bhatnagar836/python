import string


str1 = "1234567890"
str2 = "abcdefghijklmnopqrstuvwxyz"


def missingCharacters(s):
    st1 = ""
    st2 = ""
    for i in s:
        if i.isalpha():
            st2 = st2 + i
        else:
            st1 = st1 + i
    print(st1, "\n", st2)


    string1 = set(str1)-set(st1)
    print(string1)
    string2 = set(str2)-set(st2)
    print(string2)
    sorted_s1 = ''.join(sorted(string1))
    print(sorted_s1)
    sorted_s2 = ''.join(sorted(string2))
    print(sorted_s2)
    s = sorted_s1+sorted_s2
    print(s)





missingCharacters("7985interdisciplinary12")
# 0346bfghjkmoquvwxz