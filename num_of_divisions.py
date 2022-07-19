# kata7
def divisions(dividend, divisor):
    counter = 0
    while dividend >= divisor:
        quotient = dividend / divisor
        print(quotient)
        counter += 1
        dividend = quotient
    print(counter)
    return counter


divisions(9999, 3)

