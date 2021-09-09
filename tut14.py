# var1=6
# var2=56
# print("Enter a number for comparison")
# var3=int(input()) #by default input() will take string, so we have to typecast if we want to store integer to var3

# IF ELSE LADDER
# if var3>var2: #colon(:) means we want to enter into this if statement
#     print("Greater")
# elif var3==var2:
#     print("Equal")
# else:
#     print("Lesser")

# IF ELSE & LIST
# list1=[5,3,8]
# if 4 in list1:
#            print("Yes 4 is present in the list")
# elif 15 not in list1:
#            print("No,15 is not present in the list")

# Challenge :
# Take age as input from the user and if age>18-user is allowed to drive else not and in case age is equal to 18- we can't decide , so as user to come to office for physical examination
# print("Please enter your age")
age=int(input("Please enter your age"))
if age>18:
    print("You are allowed to drive")
elif age==18:
    print("Age entered is exactly 18. Sorry, we can't decide. Kindly come to the office for physical examination")
else:
    print("You are not allowed to drive and are also not eligible to apply for a driving licence")
