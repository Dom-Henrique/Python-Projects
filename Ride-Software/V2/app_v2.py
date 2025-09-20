# Banco de dados
from reg_log_v2 import *
from functions_v2 import *

user_data = {'Username': [], 'E-mail': [], 'Password': []} # Vai armazenar os dados de cadastro e será usado para percorrer
rides_data = {'Origin': [], 'Destiny': [], 'Date of Ride': [], 'Time of Ride': [], 'Vacancies': [], 'Value per Vacancy': []}

print('WELCOME TO\nRIDE SOFTWARE!')
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
    
main_menu = int(input("Please, choose one options below:\n\
1 - Ride register\n\
2 - List all rides availbles\n\
3 - Search Ride by origin and destiny locations\n\
4 - Vacation Reserv\n\
5 - Cancel Ride\n\
6 - Ride Remove\n\
7 - Ride Details\n\
8 - Show Rides\n\
9 - Log out\n"))

if main_menu == 1:
    print('Option choosed: Ride register')
    origin = input('Insert your ride origin: ')
    destiny = input('Insert your ride destiny: ')
    ride_date = input('Insert your ride date: ')
    ride_time = input('Insert your ride time: ')
    vacancies = int(input('Insert the quantity of vacancies: '))
    value_per_vacancy = float(input('Insert the price: '))
    
    Reg_Ride(origin, destiny, ride_date, ride_time, vacancies, value_per_vacancy, rides_data, username)
    
elif main_menu == 2:
    List_All_Rides(user_data, rides_data)
    
elif main_menu == 3:
    origin = input('Insert your ride origin: ')
    destiny = input('Insert your ride destiny: ')
    Search_by_Origin_Destiny(rides_data=rides_data, origin=origin, destiny=destiny)
    
elif main_menu == 4:
    email = input('Insert a valid e-mail: ')
    ride_date = input('Insert your ride date: ')
    Vac_Reserv(user_data=user_data, rides_data=rides_data, email=email, ride_date=ride_date)
    
elif main_menu == 5:
    email = input('Insert a valid e-mail: ')
    ride_date = input('Insert your ride date: ')
    Vac_Cancel(email=email, ride_date=ride_date, user_data=user_data, rides_data=rides_data)
    
elif main_menu == 7:
    email = input('Insert a valid e-mail: ')
    ride_date = input('Insert your ride date: ')
    Vac_Details(email=email, ride_date=ride_date, user_data=user_data, rides_data=rides_data)
    
elif main_menu == 8:
    email = input('Insert a valid e-mail: ')
    Show_Reg_Vac(user_data, rides_data, email)
    
elif main_menu == 9:
    Logout()