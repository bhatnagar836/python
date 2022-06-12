def name_shuffler(str_):
    list1 = (str_.split())
    print(list1[1] + " " + list1[0])
    return list1[1] + " " + list1[0]


# def name_shuffler(str_):
#     [first, last] = str_.split()
#     return last + " " + first
name_shuffler('john McClane')