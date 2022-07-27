def accum(s):
    string_given = list(s)
    print(string_given)
    new_list = []
    counter = 1
    for i in string_given[0:1]:
        new_list.append(i.upper())
        new_list.append("-")
    for i in string_given[1:len(string_given)]:
        new_list.append(i.upper())
        word = i.lower() * int(counter)
        new_list.append(word)
        new_list.append("-")
        counter += 1
    print("".join(new_list[:len(new_list)-1]))
    return "".join(new_list[:len(new_list)-1])


accum("RqaEzty")