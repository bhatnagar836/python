def print_name(a,b,c,d):
    print(a,b,c,d)

print_name("Pooja", "Krishna", "Universe", "Belief")
# What if we add one more word to above argument list, function will give error, then we have to add number of input arguments to the function

# we can have passed a list instead and can add any number of words to it
# Note: we can write it as argspooja and stars while passing and receiving are very important

def func_args(normal, *argspooja, **kwargsbeing):
# def func_args( *argspooja, normal ): # - this one would give error since args is not the last argument
    print(type(argspooja))
    # print(argspooja[0])
    print(normal)
    for item in argspooja:
        print(item)
    print("\nFollowing are some of the best humans I know:\n")
    for i, j in kwargsbeing.items():
        print(f"{i} is a {j}\n")


list1 = ["Pooja", "Krishna", "Universe", "Belief", "Love", "Respect"]
kw = {"Pooja":"Magical girl", "Aditi": "Beautiful human", "Ritu": "Kind being"}
func_args(*list1, "miracles", **kw)

# *list1 means all the elements of the list will be passed to the func_args and will store in *args (as a tuple)
# Convention - any argument other than args should be kept before and at last "*args" else it will give error

