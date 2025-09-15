# Cadastro e login
import random
import string # Permite a manipulação de dígitos

def Sign_Up(username, email, password, user_data):
    user_data['Username'].append(username)
    for email in user_data['E-mail']:
        if email not in user_data['E-mail']:
            user_data['E-mail'].append(email)
        else:
            print("You can't storage doubles e-mail adresses")
    user_data['Password'].append(password)
    
    print('User register sucessful!')
    
def Log_In(email, password, user_data):
    for email_search in user_data['E-mail']:
        if email_search == email:
            for password_search in user_data['Password']: # Só executa se o e-mail for encontrado
                if password_search == password:
                    print('User founded!')
                    print(f'Welcome')
                else:
                    print('Invalid password.')
        else:
            print('Invalid e-mail')
            
def Logout():
    print(f'Shutting down.').upper()
    quit()
            
def Pasw_Gen():
    maiusculas = list(string.ascii_uppercase)
    minusculas = list(string.ascii_lowercase)
    numeros = list(string.digits)
    special_symbols = ['!', '@', '?', '&', '(', ')', '<', '>', '[', ']', '{', '}', '#', '%', '§']
    pasw_caracteres = maiusculas + minusculas + numeros + special_symbols
    
    cont = 0
    password = ''
    while cont < 10:
        password += random.choice(pasw_caracteres)
        cont += 1
    print(f'Your password: {password}')