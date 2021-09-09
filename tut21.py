# Excersize:3
# Write a number in program (not visible to user) and take input from the user to guess the number and tell if the number input is less than or greater than the actual number and congratulate if number guessed is correct
actual_num=18
print("Guess the number(HINT: The number is a 2 digit number")
print("You have 5 chances to guess the correct number")
count=5
while(count>0):

   num = int(input("Enter a number  "))
   if(num<actual_num):
     print("Try a greater number")

   elif(num > actual_num):
     print("Try a smaller number")

   else:
       print("You Win")
       break
   count = count - 1
   print("Guesses left = ", count)

if(count==0):
    print("GAME OVER")










