import random

def pasw_gen():
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' 'v', 'w', 'x', 'y', 'z']
    simbolos = ['!', '?', '@', '#', '$', '&']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    senha = ''
    i = 0
    todos_possiveis = letras + simbolos + numeros
    
    while i < 8:
        senha += random.choice(todos_possiveis)
        i += 1
        
    print(f'Sua senha é {senha}')
    
def save_pasw(saved_senhas, senha):
    choice = int(input('Deseja salvar a senha?\n1 - Sim\t2 - Não\n'))
    if choice == 1:
        pasw_name = input('Digite o nome da sua senha: ')
        saved_senhas['Password Names'].append(pasw_name)
        saved_senhas['Password'].append(senha)
        
        print('Senha salva com sucesso!')
        
    else:
        pass
    
def register(email, password, users):
    users['E-mail'].append(email)
    users['Password'].append(password)
    print(f'Cadastro bem-sucedido!')
    
def login(email, password, users):
    while True:
        if email in users['E-mail']:
            if password in users['Password']:
                print('Login bem-sucedido!')
                break
            else:
                print('Tente novamente!')