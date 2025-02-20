
with open("pooja.txt") as f: #opens as well as closes the file
    a = f.readlines()
    print(a)

f = open("pooja.txt", "rt")
print(f.readline())
f.close()

