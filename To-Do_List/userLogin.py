from userRegister import *

class userLogin: # Usa os dados inseridos na classe anterior
    def userLogin():
        userName = input('Username: ')
        userEmail = input('E-mail: ')
        userPassword = input('Password: ')
        for i in usersTodolist:
            if userName in usersData or userEmail in usersData:
                if userPassword in usersData:
                    print(f'Sucessful login!\nWelcome, {userName}')
            else:
                print("User don't exist")
            
userLogin()