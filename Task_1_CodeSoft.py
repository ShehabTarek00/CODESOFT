print()
print('----------To Do List----------')
checkmark = "\u2713"

def view_list(list):
    print()
    print('Your To Do List :')
    j=1
    for i in list:
        print(j,'.',i)
        j+=1
    print() 
def remove_item(list,item):
    for i in list:
        if(item == i):
            list.remove(i)

list_of_tasks=[]

while 1:
    print()
    print('To Add Task Enter Add.') 
    print('To remove a task enter Remove.')
    print('To Update Task Enter Update.')
    print('To Mark a Task that Done Enter Mark.')
    print('To View a Tasks Enter View.')
    print('To Close enter Close.')
    option=input('Enter : ')
    while(option not in ['Add','add','View','view','update','Update','mark','Mark','Close','close','Remove','remove']):
        option=input('Enter Valid option : ')
    
    
    if(option == 'add' or option == 'Add'):
        task=input('Enter you New task : ')
        list_of_tasks.append(task)
        print('Your New Task Added',checkmark)
    
    if(option == 'Update' or option == 'update'):
        task=input('Enter the task you want to update : ')
        while task not in list_of_tasks:
            task=input('The task you entered is not found...Enter another task : ')
        index=0
        for i in list_of_tasks:
            if(i == task):
                i=input('Enter the updated new task : ')
                list_of_tasks[index]=i
                print('the Task has updated ',checkmark)
                view_list(list_of_tasks)
                break
            else :
                index+=1
    
    if(option == 'Mark' or option == 'mark'):
        task=input('Enter the task you have done : ')
        while task not in list_of_tasks:
            task=input('The task you entered is not found...Enter another task : ')
        index=0
        for i in list_of_tasks:
            if(i == task ):
                i+=checkmark
                i+=checkmark
                list_of_tasks[index]=i
                view_list(list_of_tasks)
                break
            else :
                index+=1

    if(option == 'View' or option == 'view'):
        view_list(list_of_tasks)
    
    if(option == 'Remove' or option == 'remove'):
        task=input('Enter the task you want to remove :')
        while (task not in list_of_tasks):
            task=input('The task you entered isnt found...Enter another task :')

        remove_item(list_of_tasks,task)    
        print('The Task deleted ',checkmark)

    if(option == 'Close' or option == 'close'):
        heart='❤️'
        print('Thanks for using ',heart)
        break
        





