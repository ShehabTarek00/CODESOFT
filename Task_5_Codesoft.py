import sys
checkmark = "\u2713"


class person :
    def __init__(self,name,phone_number,email,address):
        self.name=name
        self.phone_number=phone_number
        self.email=email
        self.address=address


    def get_name(self):
        self.name=input('enter name : ')
    def get_phone_number(self):
            self.phone_number=input('enter phone_number : ')
    def get_email(self):
        self.email=input('enter email : ')
        
    def get_address(self):
        self.address=input('enter address : ')
        
    def print_info(self):
        print()
        print('Name :',self.name)
        print('Phone number : ',self.phone_number)
        print('eEmail : ',self.email)
        print('Address : ',self.address)
        print()


print('----------------Conatct List----------------')
print()
print()
print()


names=[]

turn=1
while turn :
    one=person(0,0,0,0)
    print()
    print('To Add Contact Enter "add"')
    print('To View The Contact List Enter "view"')
    print('To Update Contact Enter "update"')
    print('To Delete Contact Enter "delete"')
    print('To Search Contact Enter "search"')
    print('To Close the Contact List Enter "close"')
    print()
    choice=input('Enter : ')

    if(choice == 'add'):
        one.get_name()
        one.get_phone_number()
        one.get_email()
        one.get_address()
        names.append(one)
        print()
        print('The Contact Added',checkmark)
        print()

    if(choice == 'view'):
        for i in names :
            i.print_info()
    
    if(choice == 'update'):
        contact=input('Enter the name of the contact you want to update : ')
        for i in names :
            if(i.name == contact ):
                new=input('which info you want to update :')
                if(new == 'name'):
                    i.get_name()
                elif(new == 'phone' or new == 'phone number'):
                    i.get_phone_number()
                elif(new == 'email'):
                    i.get_email()
                elif(new == 'address'):
                    i.get_address()
        print()
        print('The Contact Updated',checkmark)
        print()

    

    if( choice == 'search'):
        contact=input('Search by name or phone number : ')
        for i in names :
            if(i.name == contact or i.phone_number == contact ):
                i.print_info()

    if( choice=='delete'):
        deleted=input('Enter the name of the contact you want to delete : ')
        for i in names :
            if(i.name == deleted):
                names.remove(i)
        print()
        print('the Contact Deleted',checkmark)
        print()
    
    if(choice == 'close'):
        sys.exit()

        




    
    
    
    
    

