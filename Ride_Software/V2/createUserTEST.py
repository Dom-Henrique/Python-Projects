"""# Função para criar usuário

def createUser():
    global user 
    user = []
    specifUser = {'Name': '', 'E-mail': '', 'Password': ''}
    # Listas com dicionários são mais interessantes de se usar devido a fácil navegação e facilitação no armazenamento de dados
    
    # Nome completo
    global username 
    username = input('Insert your complete name: ')
    specifUser['Name'] = username
    
    # E-mail deve ser único
    global user_email
    user_email = input('Insert a valid e-mail: ')
    user_email = user_email.lower() # Vai converter tudo em letras minúsculas
    if '@' in user_email and '.com' in user_email:
        for i in specifUser:
            for j in 
    else:
        print('[INVALID E-MAIL]')
    # Senha
    global user_password
    user_password = input('Insert a password: ')
    specifUser['Password'] = user_password
    user.append(specifUser)
    print(specifUser)

createUser()

# Seria interessante que houvesse um looping"""