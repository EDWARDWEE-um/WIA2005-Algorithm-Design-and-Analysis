player1 = str(input("P1 Enter :"))
player2 = str(input("P2 Enter :"))

def game(player1,player2):
    if player1 == 'rock':
        if player2 == 'paper':
            print('Player 2 wins !')
        elif player2 =='rock':
            print('Its a draw !')
        elif player2 == 'scissors':
            print(' Player 1 wins !')
    elif player1 == 'scissors':
        if player2 == 'paper':
            print('Player 1 wins !')
        elif player2 =='scissors':
            print('Its a draw !')
        elif player2 == 'rock':
            print(' Player 2 wins !')
    elif player1 == 'paper':
        if player2 == 'scissors':
            print('Player 2 wins !')
        elif player2 =='paper':
            print('Its a draw !')
        elif player2 == 'rock':
            print(' Player 1 wins !')
            
game(player1,player2)