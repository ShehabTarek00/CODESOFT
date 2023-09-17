import random
turn=1
user_score=0
com_score=0
while (turn):
    print('Rock-Paper-Scissors Game')
    print('if you want Rock enter (r)')
    print('if you want Scissor enter (s)')
    print('if you want Paper enter (p)')

    user_turn=input('it is your turn : ')
    com_set={'scissor','rock','paper'}
    com_turn=random.choice(tuple(com_set))
    
    if(user_turn == 'r'):
        user_turn='rock'
    elif (user_turn == 'p'):
        user_turn ='paper'
    elif(user_turn == 's'):
        user_turn ='scissor'


    if ((user_turn == 'rock' and com_turn == 'rock') or (user_turn == 'scissor' and com_turn == 'scissor') or (user_turn == 'paper' and com_turn == 'paper')) :
       print()
       print('it is DRAW !!')
       print()
       print('the Computer has chosen : ',com_turn)
       print()
       print('You have chosen : ',user_turn)
       print()
       user_score+=1
       com_score+=1
       print('Your score : ',user_score)
       print()
       print('The Computer score : ',com_score)
       print()
    


    elif ((user_turn == 'rock' and com_turn == 'paper') or (user_turn == 'scissor' and com_turn =='rock') or (user_turn == 'paper' and com_turn == 'scissor')):
        print()
        print('The Computer Won !! ')
        com_score+=1
        print()
        print('the Computer has chosen : ',com_turn)
        print()
        print('You have chosen : ',user_turn)
        print()
        print('Your score : ',user_score)
        print()
        print('The Computer score : ',com_score)
        print()
    elif ((user_turn == 'rock' and com_turn == 'scissor') or (user_turn == 'scissor' and com_turn == 'paper') or (user_turn == 'paper' and com_turn == 'rock')):
        print()
        print('You Won !! ')
        print()
        user_score+=1
        print('the Computer has chosen : ',com_turn)
        print()
        print('You have chosen : ',user_turn)
        print()
        print('Your score : ',user_score)
        print()
        print('The Computer score : ',com_score)
        print()
    print('Do you want play again ? ')
    turn=input('Yes or No : ')
    if(turn == 'yes' or turn == 'y'):
        turn =1
    else :
        turn=0
        heart='❤️'
        print()
        print('Thanks for playing',heart)
    

