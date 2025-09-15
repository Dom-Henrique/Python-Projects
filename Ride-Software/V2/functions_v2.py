from reg_log_v2 import *

def Reg_Ride(origin, destiny, ride_date, ride_time, vacancies, value_vacancy, rides_data, username):
    rides_data['Origin'].append(origin)
    rides_data['Destiny'].append(destiny)
    rides_data['Date of Ride'].append(ride_date)
    rides_data['Time of Ride'].append(ride_time)
    rides_data['Vacancies'].append(vacancies)
    rides_data['Value per Vacancy'].append(value_vacancy)
    
    print('Sucessful register!')
    print(f'Congratulations, {username}! You registred a ride!')
    
def List_All_Rides(user_data, rides_data):
    print('ALL RIDES AVAILBLE')
    print(f'Rider Name: {user_data['Username']}')
    print(f'Origin: {rides_data['Origin']}')
    print(f'Destiny: {rides_data['Destiny']}')
    print(f'Date of Ride: {rides_data['Date of Ride']}')
    print(f'Time of Ride: {rides_data['Time of Ride']}')
    print(f'Vacancies: {rides_data['Vacancies']}')
    print(f'Value per Vacancy: {rides_data['Value per Vacancy']}')
    
def Search_by_Origin_Destiny(origin, destiny, rides_data):
    for origin_search in rides_data['Origin']:
        if origin == origin_search:
            for destiny_search in rides_data['Destiny']:
                if destiny == destiny_search:
                    origins = []
                    destinies = []
                    origins.append(origin)
                    destinies.append(destiny)
                    print(f'Origin: {origins}')
                    print(f'Destiny: {destinies}')
                    
def Vac_Reserv(email, ride_date, user_data, rides_data):
    for email_search in user_data['E-mail']:
        if email_search == email:
            for ride_date_search in user_data['Date of Ride']:
                if ride_date_search == ride_date:
                    print(f'Availble rides:').upper()
                    print(f'Ride founded!')
                    print(f'Rider e-mail: {email}')
                    print(f'Ride Origin: {rides_data['Origin'].index(email)}')
                    print(f'Ride Destiny: {rides_data['Destiny'].index(email)}')
                    print(f'Date of Ride: {rides_data['Date of Ride'].index(email)}')
                    print(f'Time of Ride: {rides_data['Time of Ride'].index(email)}')
                    print(f'Vacancies: {rides_data['Vacancies'].index(email)}')
                    print(f'Value per Vacancy: {rides_data['Value per Vacancy'].index(email)}')
                    
                    rides_data['Vacancies'].index(email) -= 1
                    if rides_data['Vacancies'].index(email) == 0:
                        print("Sorry, we don't have vacancies.")
                    else:
                        print('Sucessful reserve!')
                        
def Vac_Cancel(email, ride_date, user_data, rides_data):
    for email_search in user_data['E-mail']:
        if email_search == email:
            for ride_date_search in user_data['Date of Ride']:
                if ride_date_search == ride_date:
                    rides_data['Vacancies'].index(email) += 1
                    
                    print(f"Reserve canceled!")
                    
def Vac_Remove(rides_data, ride_date):
    for ride_date_search in rides_data['Date of Ride']:
        if ride_date_search == ride_date:
            index_ride = rides_data['Date of Ride'].index(ride_date_search)
            rides_data['Origin'].delete(index_ride)
            rides_data['Destiny'].delete(index_ride)
            rides_data['Date of Ride'].delete(index_ride)
            rides_data['Time of Ride'].delete(index_ride)
            rides_data['Vacancies'].delete(index_ride)
            rides_data['Value per Vacancy'].delete(index_ride)
            print("Vacancy removed!").upper()
            
def Vac_Details(email, ride_date, user_data, rides_data):
    for email_search in user_data['E-mail']:
        if email_search == email:
            for ride_date_search in user_data['Date of Ride']:
                if ride_date_search == ride_date:
                    print(f'Availble rides:').upper()
                    print(f'Ride founded!')
                    print(f'Rider e-mail: {email}')
                    print(f'Ride Origin: {rides_data['Origin'].index(email)}')
                    print(f'Ride Destiny: {rides_data['Destiny'].index(email)}')
                    print(f'Date of Ride: {rides_data['Date of Ride'].index(email)}')
                    print(f'Time of Ride: {rides_data['Time of Ride'].index(email)}')
                    print(f'Vacancies: {rides_data['Vacancies'].index(email)}')
                    print(f'Value per Vacancy: {rides_data['Value per Vacancy'].index(email)}')
                    
def Show_Reg_Vac(user_data, rides_data, email): # Caronas cadastradas do usuário logado
    for email_search in user_data['E-mail']:
        if email_search == email:
            print(f'Availble rides:').upper()
            print(f'Ride founded!')
            print(f'Rider e-mail: {email}')
            print(f'Ride Origin: {rides_data['Origin'].index(email)}')
            print(f'Ride Destiny: {rides_data['Destiny'].index(email)}')
            print(f'Date of Ride: {rides_data['Date of Ride'].index(email)}')
            print(f'Time of Ride: {rides_data['Time of Ride'].index(email)}')
            print(f'Vacancies: {rides_data['Vacancies'].index(email)}')
            print(f'Value per Vacancy: {rides_data['Value per Vacancy'].index(email)}')
            
