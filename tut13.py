# Defining set
set1= set() #This will make set1 an empty set
# print(type(set1))

# set2_using_list=set([1,3,5])
# print(set2_using_list)
# print(type(set2_using_list))

# Another way to write set using list
# l1={1,4,7}
# set3_using_l1=set(l1)
# print(set3_using_l1)

set1.add(1)
set1.add(2)
set1.add(2)#adding 2 one more time but since it is a set it won't appear two times
print(set1)
s1=set1.union({3})
print(s1)
print(set1, s1 )
s2=set1.intersection({2,3,4,6})
print(s2)
print(len(set1))
print(min(set1))
print(max(set1))
print(set1.isdisjoint(s1))# gives false because they have a common element which is 91
set1.remove(2)
set1.remove(1)
print(set1)
print(set1.isdisjoint(s1))
