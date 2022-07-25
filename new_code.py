def isValid(formula):
    if 7 or 8 in formula:
        if (1 and 2 in formula) or (3 and 4 in formula):
            print(False)
        else:
            print(True)

        # if 5 and 6:
        #     # if (1 and !2) or (2 and !1)
        #     # print(True)
        #     pass
    # print(True)


isValid([7, 8, 4])
isValid([5, 6, 7, 8, 2, 4])
