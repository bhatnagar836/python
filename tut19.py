# i=0
# # While (true) or (1) is an infinte while loop
# while(True):
#     if i<5:
#         i = i + 1
#         continue
#
#
#     print(i, end="  ")
#     if i==25:
#        break # stop the loop
#     i=i+1

# Quiz: take input from user till input entered is greater than 100
print("Enter a number")
while(True):
 inp = int(input())
 if inp>100:
     print("Congo! You have entered", inp , " which is greater than 100",)
     break
 else:
     print("Try again")
     continue
