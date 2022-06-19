def rps(p1, p2):
    if p1 == 'scissors':
        if p2 == 'paper':
            print('Player 1 won!')
            return 'Player 1 won!'
        elif p2 == 'rock':
            print('Player 2 won!')
            return 'Player 2 won!'
        else:
            print('Draw!')
            return 'Draw!'
    elif p1 == 'paper':
        if p2 == 'rock':
            print('Player 1 won!')
            return 'Player 1 won!'
        elif p2 == 'scissors':
            print('Player 2 won!')
            return 'Player 2 won!'
        else:
            print('Draw!')
            return 'Draw!'
    elif p1 == 'rock':
        if p2 == 'scissors':
            print('Player 1 won!')
            return 'Player 1 won!'
        elif p2 == 'paper':
            print('Player 2 won!')
            return 'Player 2 won!'
        else:
            print('Draw!')
            return 'Draw!'
    else:
        print('WRONG INPUT')
        return 'WRONG INPUT'


rps('rock', 'scissors')
rps('scissors', 'rock')
rps('rock', 'rock')