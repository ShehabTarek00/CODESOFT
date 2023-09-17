import random
import sys
heart='❤️'
x={'a','b','c','d','e','f','g','h',
   'i','j','k','l','m','n','o','p',
   'q','r','s','t','u','v','w','x','y','z',
   '0','1','2','3','4','5','6','7','8','9'}
y=''
turn=1
while turn :
    l=int(input('Enter the length of the password : '))
    while l<=0:
        l=int(input('Invalid length!!...Enter a valid length : '))

    for i in range(l):
        c=random.choice(tuple(x))
        y+=c


    print('Your New Password : ',y)
    turn=input('Do you like this generated Password ? \n if no Enter no Else enter yes : ')
    if(turn == 'no'):
        turn=1
    else :
        print('Thanks for using',heart)
        sys.exit()
