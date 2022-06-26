def build_string(*args):
    print("I like {}!".format(", ".join(args)))
    return "I like {}!".format(", ".join(args))


build_string('Cheese','Milk','Chocolate')