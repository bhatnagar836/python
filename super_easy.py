def problem(a):
    result = isinstance(a, str)
    if result:
        print("Error")
        return "Error"
    else:
        print((50 * a) + 6)
        return (50 * a) + 6


problem(1)
problem("hello")