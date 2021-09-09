# a=9
# b=8
# c= sum((a,b))
# print(c)

# def function1():
#     print("Hello! You are inside function1")
# print(function1())
# function1()
# function1()
# function1()

def func2(a,b):
    """This is a docstring of this function. It tells what the function is about and this fuction is used to print the sum"""
    print("The sum of a and b is ", a+b)
func2(6,4)
print(func2.__doc__)



# def avg(a,b):
#     a=int(input("Enter a\n"))
#     b = int(input("Enter b\n"))
#     average=(a+b)/2
#     print("The avg of ",a," and ", b, " is ", average)
# avg("a", "b")


# def avg2(a,b):
#     a=int(input("Enter a\n"))
#     b = int(input("Enter b\n"))
#     average = (a + b) / 2
#     print("The avg of ", a, " and ", b, " is ", average)
# # Following is trying to store the results in avariable , when we print v, it will give "none", because funtion is not returning anything
# v=avg2("a","b")
# print(v)



# def avg2(a,b):
#     a=int(input("Enter a\n"))
#     b = int(input("Enter b\n"))
#     average = (a + b) / 2
#     print(average)
#     return average
#
# # Now, when we print "v", we won't get "none" because the function is returning a value which is stored in "v"
# v=avg2("a","b")
# print(v)





