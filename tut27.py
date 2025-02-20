# FILE READING
fptr=open("pooja.txt","rt")
# Reaaline Function
# print(fptr.readline())
# print(fptr.readline())
# print(fptr.readline())

# Readlines Function
print(fptr.readlines())

# Folloing is to read file line by line
# for line in fptr:
#     print(line)

# content=fptr.read()
# print(content)

# Following is to read file character by character
# content=fptr.read()
# for line in content:
#     print(line)



# Following will print 3 characters
# content=fptr.read(3)
# print(content)

# Following will print 5 more characters
# content=fptr.read(5)
# print(content)

# Following will print 1 and then all the characters
# content=fptr.read(3540)
# print("1",content)
# Since the above line have read all the content of the file, following will only print 2 and then nothing
# content=fptr.read(50)
# print("2",content)



# f = open("pooja.txt", "w")
# f = open("pooja.txt", "a")
# f.write("She is very special to me\n")
# f.write("She is god's favourite child and a divine being")
# f.close()


fptr.close() #after doing all the operations and accesses, we must need to close the file
