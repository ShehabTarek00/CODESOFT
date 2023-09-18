import random
import sys
heart='❤️'
small_letters=list('abcdefghijklmnopqrstuvwxyz')
numbers=list('0123456789')
Capital_letters=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
Symbols=list('.,_-:;"@+-*/%^&!?><=')

Password=''
def Easy_pass(list,length):
    i=0
    pas=''
    for i in range(length):
        pas+=random.choice(tuple(list))
    return pas

def Normal_pass(list1,list2,length):
    list=list1+list2
    i=0
    pas=''
    for i in range(length):
        pas+=random.choice(tuple(list))
    return pas

def Complex_pass(list1,list2,list3,list4,length):
    list=list1+list2+list3+list4
    i=0
    pas=''
    for i in range(length):
        pas+=random.choice(tuple(list))
    return pas

turn=1
while turn :
    l=int(input('Enter the length of the password : '))
    while l<=0:
        l=int(input('Invalid length!!...Enter a valid length : '))

    Complexitiy=input('Enter the Complexity of the Password Easy or Normal or Complex : ')

    while Complexitiy not in ['easy','Easy','normal','Normal','Complex','complex']:
        Complexitiy=input('Enter valid complexitiy :')
    
    if(Complexitiy == 'easy' or Complexitiy == 'Easy' ):
        Password=Easy_pass(small_letters,l)
        print('Your New Generated Password : ',Password)

    elif(Complexitiy == 'normal' or Complexitiy == 'Normal'):
        Password=Normal_pass(small_letters,numbers,l)
        print('Your New Generated Password : ',Password)
    elif(Complexitiy == 'Complex' or Complexitiy == 'complex'):
        Password=Complex_pass(small_letters,numbers,Capital_letters,Symbols,l)
        print('Your New Generated Password : ',Password)

    turn=input('Do you want another password ? ' )
    if(turn=='yes'):
        turn=1
    else:
        turn=0
        print('Thanks for Using ',heart)
        sys.exit()

        

    
    


    