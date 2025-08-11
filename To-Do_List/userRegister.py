# User need insert your e-mail OR username and password to log in system

class userRegister:
    def userRegister():
        global usersTodolist
        usersTodolist = []
        global usersData
        usersData = {'Name': '', 'E-mail': '', 'Password': ''}
        userName = input('Username: ')
        usersData['Name'] = userName
        while True:
            userEmail = input('E-mail: ').lower()
            if '@' in userEmail and '.com' in userEmail:
                print('[E-MAIL INVÁLIDO]\nTente novamente\n')
            else:
                usersData['E-mail'] = userEmail
                break
        userPassword = input('Password: ')
        usersData['Password'] = userPassword
        
        usersTodolist.append(usersData)
        
        print(f'Usuário cadastrado com sucesso!')