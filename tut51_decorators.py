"""
def function1():
    print("Subscribe the channel now!")


# function1()
func2 = function1

del function1
# Even after deleting the function1, func2 will execute successfully, since it has a copy of function1 in itself now!
func2()
"""


def function_returner(num):
    if num == 0:
        return print
    if num == 1:
        return int


# Note : Here we can see that we can return a function via another function as well as pass the function as an argument as shown below


def executor(func):
    func("this")


executor(print)
# Note : Here we are passing a function print, that will take the place of "func" word in above function and will be executed as "print("this")"

a = function_returner(0)
print(a)

# ****************************************** DECORATORS ******************************************

# We can give any name to the decorators. Here giving "dec1"


# Usage - when we have to perform a certain task with multiple functions, we make a decorator, so that we can pass the function inside it as shown below
def dec1(func4):
    def now_exec():
        print("Executing now...")
        func4()
        print("Function executed!")
    return now_exec()  # returning the function

@dec1
def who_is_Pooja():
    print("Pooja is god's miracle child")

# who_is_Pooja = dec1(who_is_Pooja) # This line can be replaced by placing the decorator name above the function with "@" as shown above
# who_is_Pooja()
# Note: who_is_Pooja when given inside the decorator becomes the part of now_exec and will return whole now_exec as a function




