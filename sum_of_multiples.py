def sum_mul(n, m):
    sum_is = 0
    multiple = 1
    i = 1
    if n <= 0 or m <= 0:
        print("INVALID")
        return "INVALID"
    elif m > 0:
        while multiple+n <= m:
            multiple = n * i
            # print("Multiple: ", multiple)
            sum_is += multiple
            # print("Sum ", sum_is)
            i += 1
            # print("Value of i", i)
        print("Final sum is : ", sum_is)
        return sum_is
    else:
        print("INVALID")
        return "INVALID"


sum_mul(58, 59)
# sum_mul(4, -7)