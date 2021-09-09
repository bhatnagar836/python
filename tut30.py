# Excersize 4
# PATTERN PRINTING
#  Input : a number and a variable in which we can enter '0' or '1' and typecast 0 to "false" and 1 to "true"
# If input in true then print the following pattern:
# *
# **
# ***
# ****
# Else the following pattern:
# ****
# ***
# **
# *

var1=int(input("Enter a number\n"))
var2=int(input("Enter 0 for false and 1 for true\n"))
print("You have entered ",bool(var2))
if(var2==1):
    print("*\n")
else:
    print("\n*")