# Try and Except an error
# Try (if error occurs)
# Except(catch the error and let the program continue)


# If wrong inputs given, will throw error in any of given first two lines
# num1=int(input("Enter num1\n"))
# num2=int(input("Enter num2\n"))
# print("Sum of ",num1, "and", num2," is ",
#           num1+num2)


# num1=(input("Enter num1\n"))
# num2=(input("Enter num2\n"))
# print("Sum of ",num1, "and", num2," is ",
#           int(num1)+int(num2))
# If given wrong input will throw error in the above line


num1=(input("Enter num1\n"))
num2=(input("Enter num2\n"))
try:
    print("Sum of ",num1, "and", num2," is ",
          int(num1)+int(num2))
except Exception as error:
    print("ERROR OCCURRED:\n",error)

print("Very important code after this print statement")



