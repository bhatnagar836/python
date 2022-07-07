geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    new_list = []
    for items in birds:
        if items in geese:
            pass
        else:
            new_list.append(items)
    print(new_list)
    return new_list


# def goose_filter(birds):
#     print([bird for bird in birds if bird not in geese])
#     return [bird for bird in birds if bird not in geese]



goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"])
