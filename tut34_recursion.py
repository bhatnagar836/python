
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# inp = int(input("Enter a number\n"))
# out = fact(inp)
# print(out)


def fibo(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)

inp = int(input("Enter a number\n"))
out = fibo(inp)
print(out)



