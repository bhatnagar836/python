# kata7
def add10(x):
    return x + 10


def mul30(x):
    return x * 30


def chain(init_val, functions):
    if not functions:
        # print(init_val)
        return init_val
    elif len(functions) == 1:
        if functions[0] == add10:
            x = add10(init_val)
            print(x)
            return x
        elif functions[0] == mul30:
            x = mul30(init_val)
            print(x)
            return x
    elif len(functions) > 1:
        if functions[0] == add10:
            x = add10(init_val)
        elif functions[0] == mul30:
            x = mul30(init_val)
        for items in functions[1: len(functions)]:
            if items == add10:
                x = add10(x)
                # print(x)
            elif items == mul30:
                x = mul30(x)
                # print(x)
        print(x)
        return x


chain(50, [add10, mul30, add10, add10])
chain(50, [mul30])

