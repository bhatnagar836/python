# 3 clients - Harry, Rohan, Hammad
# 6 files - 3 for their food and 3 for their excersize
# function takes client name as input and what they want to log - excersize or diet

def getdate():
    import datetime
    return datetime.datetime.now()

time = getdate()

def func1():
    food_is = input("Enter Diet:\n-")
    f1.write(f"[{time}]:")
    f1.write(food_is)
    f1.write("\n")

def func2():
    excer_is = input("Enter Excersize\n-")
    f2.write(f"[{time}]:")
    f2.write(excer_is)
    f2.write("\n")

client = input("Enter name of the client\n")
op = input("Enter w to write and r to retrieve\n")
num = int(input("Enter 1 to enter diet or 2 to enter excersize\n"))
if client == "Harry":
    if op == "w" and num == 1:
        f1 = open("harry_food.txt", "a")
        func1()
        f1.close()
    elif op == "w" and num == 2:
            f2 = open("harry_ex.txt", "a")
            func2()
            f2.close()
    elif op == 'r' and num == 1:
        with open("harry_food.txt") as f:  # opens as well as closes the file
            a = f.readlines()
            print(a)
    elif op == 'r' and num == 2:
        with open("harry_ex.txt") as f:  # opens as well as closes the file
            a = f.readlines()
            print(a)
    else:
        print("Wrong operation or number entered")

elif client == "Rohan":
    if op == "w" and num == 1:
        f1 = open("rohan_food.txt", "a")
        func1()
        f1.close()
    elif op == "w" and num == 2:
            f2 = open("rohan_ex.txt", "a")
            func2()
            f2.close()
    elif op == 'r' and num == 1:
        with open("rohan_food.txt") as f:  # opens as well as closes the file
            a = f.readlines()
            print(a)
    elif op == 'r' and num == 2:
        with open("rohan_ex.txt") as f:  # opens as well as closes the file
            a = f.readlines()
            print(a)
    else:
        print("Wrong operation or number entered")
elif client == "Hammad":
    if op == "w" and num == 1:
        f1 = open("hammad_food.txt", "a")
        func1()
        f1.close()
    elif op == "w" and num == 2:
            f2 = open("hammad_ex.txt", "a")
            func2()
            f2.close()
    elif op == 'r' and num == 1:
        with open("hammad_food.txt") as f:  # opens as well as closes the file
            a = f.readlines()
            print(a)
    elif op == 'r' and num == 2:
        with open("hammad_ex.txt") as f:  # opens as well as closes the file
            a = f.readlines()
            print(a)
    else:
        print("Wrong operation or number entered")
else:
    print("No such client found")