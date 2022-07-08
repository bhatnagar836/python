# def is_lock_ness_monster(string):
#     if "tree fiddy" in string:
#         print(True)
#         return True
#     elif "three fifty" in string:
#         print(True)
#         return True
#     elif "3.50" in string:
#         print(True)
#         return True
#     else:
#         print(False)
#         return False


def is_lock_ness_monster(s):
    print(any(i in s for i in ('tree fiddy', 'three fifty', '3.50')))
    return any(i in s for i in ('tree fiddy', 'three fifty', '3.50'))


is_lock_ness_monster("Yo, I heard you were on the lookout for Nessie. Let me know if you need assistance.")