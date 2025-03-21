"""
l = 11

def func1(n):
    # l = 5 #local variable
    m = 7 #local variable
    global l
    print(l)
    l = l+10 # Usually we cannot change the value of a global variable, but in python we can do so by using global keyword
    print(l,m)
    print(n, "I love you uncoditionally!!")


func1("Hi my favourite child")
print(l)
"""

x = 89
def pooja():
    x = 21
    def miracle():
        global x # takes the control outside all the functions to the global area and searches for x and not finding any x
        x = 51
    print("Before calling miracle, value of x is ", x)
    miracle()
    print("After calling miracle, value of x is ", x)

pooja()
print(x) #goes out in search of x and creates it in case of notfinding it