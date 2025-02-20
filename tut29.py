# FILE WRITING

n = int(input("Enter how many rows?\n"))
boolean = int(input("Enter 0 for ascending traingle pattern and 1 for decending traingle pattern\n"))
print("You have entered ",bool(boolean))

if boolean == 0:
    for i in range(n+1):
        print(("*")*i)
elif boolean == 1:
    for i in range(n+1):
        print(("*")* (n-i))
