def correct(s):
    new_s = []
    for item in s:
        if item == '0':
            new_s.append('O')
        elif item == '1':
            new_s.append('I')
        elif item == '5':
            new_s.append('S')
        else:
            new_s.append(item)
    print(''.join(new_s))
    return ''.join(new_s)

# def correct(string):
#     return string.translate(str.maketrans("501", "SOI"))


correct("L0ND0N")
correct("DUBL1N")
correct("51NGAP0RE")
correct("BUDAPE5T")
correct("PAR15")
