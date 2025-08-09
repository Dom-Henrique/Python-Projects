# Função para criar usuário

def createUser():
    user = {'complete name': [], 'email': [], 'password': []}
    # Nome completo
    username = input('Insert your complete name: ')
    user['complete name'].append(username)
    # E-mail deve ser único
    user_email = input('Insert a valid e-mail: ')
    if '@' in user_email and '.com' in user_email:
        for i in user['email']:
            if i not in user['email']:
                user['email'].append(user_email)
                break
            else:
                print('[INVALID E-MAIL]\nYour e-mail needs to be unique.')
    else:
        print('[INVALID E-MAIL]')
    # Senha
    user_password = input('Insert a password: ')
    user['password'].append(user_password)
                
createUser()

# Seria interessante 