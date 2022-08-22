def friend(x):
    new_l = []
    print(x)
    for item in x:
        if len(item) == 4:
            new_l.append(item)
        else:
            pass
    return new_l
