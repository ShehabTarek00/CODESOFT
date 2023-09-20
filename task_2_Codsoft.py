def sum(n,m):
    return (n+m)
def diff(n,m):
    return (n-m)
def product(n,m):
    return (n*m)
def division(n,m):
    return (n/m)
turn=1
while (turn):
    x=int(input('Enter the first number : '))
    y=int(input('Enter the second number : '))
    o=input('Enter the operation you want to be calculated : ')
    if(o == '+' or o == 'sum' or o == 'add' or o=='plus'):
        print('the Result = ',sum(x,y))
    elif(o == '-' or o == 'difference' or o == 'minus' or o=='subtract'):
        print('the Result = ',diff(x,y))
    elif(o == '*' or o == 'x' or o == 'product' or o == 'times' or o=='multiply'):
        print('the Result = ',product(x,y))
    elif( o == '/' or o == 'division' or o=='divide'):
        div=round(division(x,y),4)
        print('the Result = ',div)
    print('Do you want another calculation ? ')
    ans=input('yes or no ? ')
    if(ans == 'yes'):
        turn=1
    elif(ans == 'no'):
        turn=0
        heart='❤️'
        print('Thanks for using',heart)