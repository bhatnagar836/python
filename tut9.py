mystr="pooja is a Good Girl"
print(mystr)
print(mystr[4])
print(len(mystr))
print(mystr[0:20])
print(mystr[0:78])# this will give string as output because string length(20) is less than 78
# print(mystr[78]) This will give error as it is not out string length
print(mystr[0:10:3]) #skip 2 character and print other character from index 0 to 10 excluding 10
print(mystr[0:])# by default print full string
print(mystr[:5])#starts with 0 index
print(mystr[:]) #print full string starting with index 0
print(mystr[::]) #by default takes third param as 1 ie. 0 characte r skipped
print(mystr[-18:-2])
# line number 13 and 15 works the same way (infact 15 is another way to write line number 13)
print(mystr[2:18])
print(mystr[::-1])
print(mystr[::-2])
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("girl"))
print(mystr.endswith("giril"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is a Good Girl", "is brilliant"))