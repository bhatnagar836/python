def ordered_count(inp):
    inp_l = list(inp)
    list2 = []
    list3 = []
    for char in inp_l:
        if char not in list2:
            new_tuple = (char, inp_l.count(char))
            list2.append(new_tuple)
        else:
            pass

    for items in list2:
        if items not in list3:
            list3.append(items)
        else:
            pass
    return list3


ordered_count("abracadabra")
