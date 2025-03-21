import random

n = 1
count_comp = 0
count_ply = 0
while(n <= 10):
    arr1 = ["snake", "water", "gun"]
    computer = random.choice(arr1)
    player = input("Enter s for snake, w for water, g for gun\n")
    print(f"Coumputer chose {computer}\n")
    if computer == 'snake':
        if player == 's':
            print("Draw")
            count_comp += 0
            count_ply += 0
        elif player == 'w':
            print("Computer got 1 point\n")
            count_comp += 1
            count_ply += 0
        elif player == 'g':
            print("Player got 1 point\n\n")
            count_comp += 0
            count_ply += 1
        n += 1
    elif computer == 'water':
        if player == 'w':
            print("Draw")
            count_comp += 0
            count_ply += 0
        elif player == 'g':
            print("Computer got 1 point\n")
            count_comp += 1
            count_ply += 0
        elif player == 's':
            print("Player got 1 point\n")
            count_comp += 0
            count_ply += 1
        n += 1
    elif computer == 'gun':
        if player == 'g':
            print("Draw")
            count_comp += 0
            count_ply += 0
        elif player == 's':
            print("Computer got 1 point\n")
            count_comp += 1
            count_ply += 0
        elif player == 'w':
            print("Player got 1 point\n")
            count_comp += 0
            count_ply += 1
        n += 1

if count_comp >count_ply:
    print(f"Computer Wins by {count_comp - count_ply}")
elif count_comp < count_ply:
    print(f"Congratulations! You win by {count_ply - count_comp}!")
else:
    print("It's a DRAW")


