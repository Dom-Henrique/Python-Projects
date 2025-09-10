# Banco de dados
from reg_log_v2 import *
user_data = {'Username': [], 'E-mail': [], 'Password': []} # Vai armazenar os dados de cadastro e será usado para percorrer
rides_data = {'Origin': [], 'Destiny': [], 'Date of Ride': [], 'Time of Ride': [], 'Vacancies': [], 'Value per Vacancy': []}

print('WELCOME TO\nRIDESOFTWARE!')
print('*'*50)

options = int(input('Please, choose one of options below:\n\
1 - Sign Up\n\
2 - Log In\n'))


if options == 1:
    print('Option choosed: Sign Up')
    username = input('Name:\n')
    while True:
        email = input('E-mail:\n')
        if '@' not in email and '.com' not in email:
            print('Insert a valid e-mail adress.')
        else:
            break
    pasw_option = int(input('You want create a password yourself or generate one?\n1 - Create myself\t2 - Generate\n'))
    if pasw_option == 1:
        while True:
            print('Password can only have up to 10 characters.')
            password = input('Password:')
            if len(password) == 10:
                break
            else:
                print('Please, try again.\n')
        Sign_Up(username, email, password, user_data)
    elif pasw_option == 2:
        Pasw_Gen()
        Sign_Up(username, email, Pasw_Gen, user_data)
        
elif options == 2:
    print('Option choosed: Sign Up')
    while True:
        email = input('E-mail:\n')
        if '@' not in email and '.com' not in email:
            print('Insert a valid e-mail adress.')
        else:
            break
    pasw_option = int(input('You want create a password yourself or generate one?\n1 - Create myself\t2 - Generate\n'))
    if pasw_option == 1:
        while True:
            print('Password can only have up to 10 characters.')
            password = input('Password:')
            if len(password) == 10:
                break
            else:
                print('Please, try again.\n')
        Log_In(email, password, user_data)
    elif pasw_option == 2:
        Pasw_Gen()
        Log_In(email, Pasw_Gen, user_data)
        
else:
    print('ERROR')