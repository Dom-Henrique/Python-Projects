from modules import *
saved_senhas = {'Password Names': [], 'Password': []}
users = {'E-mail': [], 'Password': []}

while True:
    email = input('E-mail: ')
    if '@' not in email and '.com' not in email:
        print('Insira um e-mail válido!')
    else:
        break

desejo_usuario = int(input('Deseja gerar uma senha?\n1 - S\t2 - N\n'))
if desejo_usuario == 1:
    gerar_senha = pasw_gen()
    salvar_senha = save_pasw(saved_senhas, pasw_gen)
    register(email, gerar_senha.senha, users)
elif desejo_usuario == 2:
    senha = input('Senha: ')
    register(email, senha, users)

deseja_login = int(input('Deseja fazer login?\n1 - S\t2 - N\n'))
if deseja_login == 1:
    login(email, senha)
elif deseja_login == 2:
    print('Programa encerrado.')
    quit()