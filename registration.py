'''
Registration 

1 class to create user template for registration
2 create def to open file and write user info into it
'''
first_name = ''
last_name = ''
email = ''
username = ''
password = ''

class Registration():
    
    def __init__(self,first_name,last_name,email,username,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        
    def Add_User(self):
        
        fhandle.write('\n')
        fhandle.write('First Name: ')
        fhandle.write(self.first_name)
        fhandle.write('\nLast Name: ')
        fhandle.write(self.last_name)
        fhandle.write('\nEmail: ')
        fhandle.write(self.email)
        fhandle.write('\nUsername: ')
        fhandle.write(self.username)
        fhandle.write('\nPassword: ')
        fhandle.write(self.password)
        fhandle.write('\n')
        
fhandle = open("test.txt","a")

new_user = input

new_user = Registration(first_name,last_name,email,username,password)

fhandle.write(new_user.Add_User())
