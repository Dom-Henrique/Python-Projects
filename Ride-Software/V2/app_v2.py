from reg_log_v2 import *
# from functions_v2 import *

username = input('Insira seu nome: ')
useremail = input('Insira um e-mail válido: ')
userpassword = input('Insira uma senha: ')

x = UserRegister(username, useremail, userpassword)
UserLogin(x)