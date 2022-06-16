# def xor(a, b):
#     print(True) if (a == True and b == False) or (a == False and b == True) else print(False)
#     return True if (a == True and b == False) or (a == False and b == True) else False
#

def xor(a, b):
    print(a != b)
    return a != b


xor(False, False)
xor(True, False)
xor(False, True)
xor(True, True)