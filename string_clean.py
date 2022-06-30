def string_clean(s):
    """
    Function will return the cleaned string
    """
    new_s = ""
    for item in s:
        if item.isnumeric():
            pass
        else:
            new_s = new_s + item
    print(new_s)
    return new_s


string_clean("E3at m2e2!!")
