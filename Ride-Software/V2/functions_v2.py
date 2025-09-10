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
                    print(f'Origin: {origin}')
                    print(f'')