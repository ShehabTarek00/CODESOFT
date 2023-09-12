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
       print('it is DRAW !!')
       print('the Computer has chosen : ',com_turn)
       print('You have chosen : ',user_turn)
       user_score+=1
       com_score+=1
       print('Your score : ',user_score)
       print('The Computer score : ',com_score)
    


    elif ((user_turn == 'rock' and com_turn == 'paper') or (user_turn == 'scissor' and com_turn =='rock') or (user_turn == 'paper' and com_turn == 'scissor')):
        print('The Computer Won !! ')
        com_score+=1
        print('the Computer has chosen : ',com_turn)
        print('You have chosen : ',user_turn)
        print('Your score : ',user_score)
        print('The Computer score : ',com_score)
    elif ((user_turn == 'rock' and com_turn == 'scissor') or (user_turn == 'scissor' and com_turn == 'paper') or (user_turn == 'paper' and com_turn == 'rock')):
        print('You Won !! ')
        user_score+=1
        print('the Computer has chosen : ',com_turn)
        print('You have chosen : ',user_turn)
        print('Your score : ',user_score)
        print('The Computer score : ',com_score)
    print('Do you want play again ? ')
    turn=input('Yes or No : ')
    if(turn == 'yes'):
        turn =1
    elif(turn == 'no'):
        turn=0
    

