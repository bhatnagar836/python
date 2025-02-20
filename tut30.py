f = open("pooja.txt")
print(f.tell())  # tells the where the file pointer is pointing currently
print(f.readline())
print(f.tell(), "\n")

print("**************************************************************", "\n")
f.seek((11)) # brings the file pointer to the location specified
print(f.readline())
f.seek((0))
print(f.readline())

f.close()
