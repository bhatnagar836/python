# FILE WRITING
f=open("pooja.txt", "w")
# Getting number of characters printed
f.write("Pooja girl is a very good \n")
f.write("Pooja likes walking in nature")
# b=f.write("Pooja has started doing meditation also\n")
# print(b)

# FILE APPEND
# f = open("pooja.txt", "a")
# f.write("Pooja does excersize also \n")
# c=f.write("Pooja does excersize also \n")
# print(c)

# HANDLE READ AND WRITE BOTH
fptr1=open("pooja2.txt", "r+")
print(fptr1.read())
fptr1.write("Thankyou\n")










f.close()