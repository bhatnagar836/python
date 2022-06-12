def even_or_odd(number):
    # print("Even") if number % 2 == 0 else print("Odd")
    print("Odd") if number % 2 else print("Even")
    return "Even" if number % 2 == 0 else "Odd"


even_or_odd(31)