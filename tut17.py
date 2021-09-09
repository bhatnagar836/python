# list1=["Harry","Larry","Carry", "Marie"]
# Following will be hectic method to print each item of the list
# print(list1[0],list1[1],list1[2],list1[3])

# Loops can make our work easy

# FOR LOOP
# for element in list1:
#     print(element)


# List of list
# list2=[["Harry",1],["Larry",2],["Carry",6], ["Marie",10]]
# for items in list2:
#     print(items)
# for element, toffees in list2:
#     print( toffees,element)

# tup1=("Harry","Larry","Carry", "Marie")
# # Note: in place of elements we can write any other variable ( like items, thing, stuff etc)
# for stuff in tup1:
#     print(stuff)

# list2=[["Harry",1],["Larry",2],["Carry",6], ["Marie",10]]
# dict2=dict(list2)
# print(dict2)
# for names in dict2:
#     print(names)
# Following will give error
# for names, toffees in dict2:
 #        print(names,toffees)
 #Instead of above , use the following which contains item(), it will work fine
# for names, toffees in dict2.items():
#         print(names,"have",toffees ,"toffees")

# QUIZ: Make a list, print only items (elements) which are numbers that too greater than 6

items=[int, float, "Pooja", "Aditi", 5, 91, 3, "Sonali", 16, 2, "Ritu", 21,"You"]
for element in items:
        if str(element).isnumeric() and element>6:
                print(element)