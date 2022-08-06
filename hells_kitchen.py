def gordon(a):
    new_list = []
    a = a.upper()
    a = a.replace("A", "@")
    a = a.replace('E', '*')
    a = a.replace('I', '*')
    a = a.replace('O', '*')
    a = a.replace('U', '*')
    print(a)
    x = a.split()
    for items in x:
        items += "!!!!"
        new_list.append(items)
    print(" ".join(new_list))
    return " ".join(new_list)



gordon('What feck damn cake')