# Create a dictionary and take input from the user and return the meaning of the word from the dictionary
myDict={"accord":"concurrence of opinion",
       "evident":"clearly revealed to the mind or the senses or judgment",
       "appoint":"assign a duty, responsibility, or obligation to",
       "instance":"an occurrence of something",
       "project":"a planned undertaking"}
print("Enter a word to find meaning from the dictionary")
word=input()
print(word,"meaning:", end=" ")
print(myDict[word])
# OR
# print(myDict.get(word))