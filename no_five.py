def dont_give_me_five(start, end):
    new_l = []
    for i in range(start, end+1):
        if str(5) in str(i):
            pass
        else:
            new_l.append(i)
            i += 1
    print(new_l)
    print(len(new_l))
    return len(new_l)


# def dont_give_me_five(start, end):
#     return len([num for num in range(start, end+1) if '5' not in str(num)])

dont_give_me_five(52, 72)