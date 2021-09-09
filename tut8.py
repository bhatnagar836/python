# var1="Hello World"
# var2=4
# var3=30.5
# print(var1)
# print(type(var1))
# print(var2)
# print(type(var2))
# print(var3)
# print(type(var3))
# print(var2+var3)
#
# var4=" Pooja"
# print(var1+var4)
#
# var5=" 54"
# var6=" 32"
# # Following will result in concatenation of 54 and 32
# print(var5+ var6)
# # Following will result 86 due to typecasting
# print(int(var5)+int (var6))
# print(float(var5)+float (var6))
#
# print(10*"Hello Pooja\n") #prints Hello Pooja 10 times
# # But writing print(100*int(var5)+int (var6)) will multiply var 5 by 100 and result changes to 5432
# print(100 * int(var5) + int (var6))
# print(100 * (int(var5) + int (var6)))
# print(100 * str(int(var5) + int (var6))) #will print result of addtion(ie.86) hundred times
#
# # Taking Input from User
# print("Enter your number")
# inpnum=input()
# print("You entered", inpnum, end=" \n ")
# # Following will give error as inpnum is a string
# # print("You entered", inpnum +10)
# #Typecasting will solve the problem
# print("After adding 10 number will be",int( inpnum) +10)

# Excersize : Make a calculator that will add 2 numbers given by users
print("Enter 2 numbers to be added\n")
num1=input()
num2=input()
print("Sum of the given numbers is " ,int(num1)+int(num2))