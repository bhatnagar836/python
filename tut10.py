grocery=["Arhar", "Rice", "Atta", "Deodrant", "Sabji", 87]
print(grocery)
print(grocery[3])
#Following will give error because there is no element at 6th location(Note:index starts with 0)
# print(grocery[6])
numbers=[2,7,9,11,3]
print(numbers)
print(numbers[2])
# Following will return none but if we sort first and then print the numbers then the numbers will be sorted
# print(numbers.sort())

# SORT AND REVERSE FUNCTION
# numbers.sort()
# print(numbers)
# # Following will reverse the numbers(which are already sorted). Giving output in descending order
# numbers.reverse()
# print(numbers)

# # SLICING
# print("Slicing")
# print(numbers[:]) # by default values will be print(numbers[0:5] ie. start index and length of list)
# print(numbers[0:])
# print(numbers[:5])
# print(numbers[1:4])#starts with index=1  and print excluding 4
# # Following works fine with -ve  sign only when other two parameters are not specified(ie. having default values)
# print(numbers[::-1])
# print(numbers[::-2])
# print(numbers[::-3])
# # Following returns blank list(ie. steps param not working due to -ve value)
# print(numbers[2:5:-1])
# # We can write 3rd param in +ve steps as much as we want
# print(numbers[1:5:2]) #starts with index 1 till index 4(index 5 excluded) skipping 1 element
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))


# # APPEND(Adding element to the list at the last)
# numbers2=[] # we can declare a blank list and then append or we can also append to the list having element already
# numbers2.append(4)
# numbers2.append(2)
# numbers2.append(21)
# numbers2.append(6)
# numbers2.append(5)
# numbers2.append(25)
# print(numbers2)
# # INSERT(Adding element to a specific index (need not be compulsorily at the last))
# # First param specifies the index (where we want to insert) second param specifies the element to be inserted
# numbers2.insert(2,3)
# numbers2.insert(3,7)
# print(numbers2)
# numbers2.insert(2,19) #this will override the above list
# print(numbers2)
# # REMOVE (Removes given element from list)
# print("Removing")
# numbers2.remove(19)
# print(numbers2)
# # POP(remove the last element from the list)
# print("Poping")
# numbers2.pop()
# print(numbers2)


# LISTS AND TUPLES
# numbers[1]=98
# print(numbers)
# Lists are mutable(can change) and tuples are immutable(can't change)
# tp=(1,2,3)
# print(tp)
# # tp(2)=5
# tup=(1,) #for one element, we have to put comma at the end (else it won't become a tuple)
# print(tup)


# SWAPPING TWO NUMBERS
a=1
b=8
# temp=a
# a=b
# b=temp
# OR we can do the following in python
a,b=b,a
print(a, b)