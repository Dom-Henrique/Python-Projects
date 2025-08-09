from createUser import *

# Login com opção de motorista ou passageiro.

def userLogin(userName, userEmail, userPassword):
    option = int(input('Deseja fazer login?\n1 - Sim\t2 - Não'))
    if option == 1:
        while True:
            userName = input('Insert your complete name: ')
            userEmail = input('Insert a valid e-mail: ')
            userPassword = input('Insert a password: ')
            if userName in users['Complete Name']:
                if userEmail in users['E-mail']:
                    if userPassword == users['Password']:
                        print(f'Suscedeed login!\nWelcome, {userName}!')
                        break
            else:
                print('[ERROR]\nPLEASE, TRY AGAIN')
                
userLogin()