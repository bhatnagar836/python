# lambda function or annymoous function - one liner functions
minus = lambda x, y: x*y*2

out = minus(2,3)
print(out)
""""
The above will be same as 
def minus(x,y):
    return x*y*2
"""

def a_first(a):
    # function returns item at 1st index
    return a[1]

# lambda with sort
a = [[4,6], [21,9], [11,1]]
# key takes a function and work according to that
# a.sort(key=a_first)


# above line can also be written as :
a.sort(key=lambda x: x[1])
print(a)
