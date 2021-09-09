# Excersize 2: Faulty calculator
# 45*3=555, 56+9=77, 56/4=4
# Apart from the above calculations other results will be right
print("Enter any of the given operator: +,-,*,/,%,**\n")

var1 = input()
var2 = int(input("Enter the operand1   "))
var3 = int(input("Enter the operand2   "))
if var1 == '*' and var2==45 and var3==3:
    print(555)
elif var1 == '+' and var2==56 and var3==9:
    print(77)
elif var1 == '/' and var2 == 56 and var3 == 4:
        print(4)
else:
    if var1=='+':
        print(var2+var3)
    elif var1 == '-':
        print(var2 - var3)
    elif var1=='*':
        print(var2*var3)
    elif var1=='/':
        print(var2/var3)
    elif var1=='%':
        print(var2%var3)
    else:
        print(var2**var3)







