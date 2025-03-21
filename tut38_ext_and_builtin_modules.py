import random
# some modules contain functions and some contains  sub modules which then contain functions
random_num = random.randint(0,5)
print(random_num)

#Following generates a number from 0 to 1
rand_num = random.random()*100 #number generated is multiplied by 100 - resulting in generating number between 0 to 100
print(rand_num)
list1 = ["Krishna", "Universe", "Mother Nature", "Pooja"]
choice = random.choice(list1)
print(choice)