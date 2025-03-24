
def print_universe(str):
    return f"Universe - {str}"


def product_is(a,b):
    return a*b


print(__name__)

if __name__ == '__main__': # To execute all the content of the file only when "main" is called i.e. value of name == "main"
    print(print_universe("Bless me"))
    out = product_is(3,7)
    print(out)