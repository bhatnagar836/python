import math
me = "Pooja"
a2 = "Bhatnagar"
a3 = "god's"
a4 = "favourite"
a5 = "child"
a = 21
# way1
# b = "This is %s %s %s %s %s %s" % (me, a2, a3, a4, a5, a)
# way2
b = "This is {5} {4} {3} {2} {1} {0}"
b1 = b.format(me, a2, a3, a4, a5, a)
print(b1)

# way3 - fstrings (makes readability easy for us)
str_with_f_string = f"This is {me} {a2} and I am {a3} {a4} {a5} born on {a} November"
print(str_with_f_string)

can_use_other_modules_funtions = f"This is {math.cos(45)}"
print(can_use_other_modules_funtions)
