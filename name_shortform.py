def abbrev_name(name):
    x = name.split()
    s_name = ""
    for items in x:
        if items[0].isupper():
            s_name += items[0]
            s_name += "."
        elif items[0].islower():
            s_name += items[0].capitalize()
            s_name += "."
    length_s = len(s_name)-1
    s_name = s_name[:length_s]
    print(s_name)
    return s_name


def abbrevName(name):
    print('.'.join(w[0] for w in name.split()).upper())
    return '.'.join(w[0] for w in name.split()).upper()


abbrev_name("david Mendieta")
abbrevName("patrick feenan")