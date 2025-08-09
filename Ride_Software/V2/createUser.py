def createUser():
    # Criar um banco de dados usando dicionários
    users = [] # Lista armazena os usuários
    dataUsers = {'Complete name': '', 'Age': '', 'E-mail': '', 'Password': ''} # Dicionário com as informações de cada usuário
    
    userName = input('Insert your complete name: ')
    dataUsers['Complete name'] = userName
    
    while True:
        userAge = int(input('Insert your age: '))
        if userAge >= 18:
            dataUsers['Age'] = userAge
            break
        else:
            print('YOU ARE MINOR\nPlease, try again\n')
    
    while True:
        userEmail = input('Insert your e-mail: ')
        if '@' in userEmail and '.com' in userEmail:
            if any(user['E-Mail'] == userEmail for user in users):
                print('[INVALID E-MAIL]\nPlease, try again')
            else:
                dataUsers['E-mail'] = userEmail
                break
        else:
            print('[INVALID E-MAIL]\nPlease, try again')
            
    userPassword = input('Create your password: ')
    dataUsers['Password'] = userPassword
    
    users.append(dataUsers)
    
    print(f'Parabéns, {userName}!\nSeu cadastro foi concluído com sucesso!')
    
createUser()