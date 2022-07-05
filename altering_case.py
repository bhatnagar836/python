def to_alternating_case(string):
    new_string = ""
    for item in string:
        if item.isupper():
            new_string = new_string + item.lower()
        elif item.islower():
            new_string = new_string + item.upper()
        else:
            new_string = new_string + item
    print(new_string)
    return new_string


to_alternating_case("1a2b3c4d5e")
to_alternating_case("HeLLo WoRLD")