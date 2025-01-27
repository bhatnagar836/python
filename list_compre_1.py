
# Find all of the numbers from 1-1000 that are divisible by 7
list1 = [i for i in range(1,1001) if i%7 == 0]
print(list1)

# Find all of the numbers from 1-1000 that have a 3 in them
three = [j for j in range(1, 1001) if "3" in str(j)]
print(three)

# Count the number of spaces in a string
count = [k for k in "sfd jhghgf guy   jhyi fsrdf" if k==" "]
print(len(count))


# Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
consonants = [c for c in sentence if c not in ['a','e','i','o','u'," "]]
print(consonants)


# Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)
items = ["hi", 4, 8.99, 'apple', ('t,b','n')]
result = [(index,item) for index,item in enumerate(items)]
print(result)

# Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_nums = [k for k in list_a if k in list_b]
print(common_nums)


# Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
sentence = "In 1984 there were 13 instances of a protest with over 1000 people attending"
words = sentence.split()
print(words)
numbers_in_sen = [k for k in words if not k.isalpha()]
print(numbers_in_sen)


# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
even_odd = ["even" if i%2 == 0 else "odd" for i in range(20)]
print(even_odd)

# Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)
list_a = [1, 2, 3,4,5,6,7,8,9]
list_b = [2, 7, 1, 12]
result = [(a,b) for a in list_a for b in list_b if a == b]
print(result)

# Find all of the words in a string that are less than 4 letters
sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'
words = sentence.split()
words_are = [i for i in words if len(i) < 4]
print(words_are)

# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
nums = [n for n in range(1,1001) if True in [True for x in range(2,10) if n%x == 0 ]]

# for n in range(1, 1001):
#     for x in range(2, 10):
#         if n % x == 0:
#             nums.append(n)
print(list(set(nums)))
