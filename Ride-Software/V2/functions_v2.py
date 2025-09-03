"""# Resto das funções
from reg_log_v2 import UserLogin
riders_rides = {'Rider Name': [], 'Rider E-mail': [], 'Origin': [], 'Destiny': [], 'Date': [], 'Time': [], 'Vacancies': [], 'Vacancies Price': []}

def RideRegister(origin, destiny, date, time, vacancies, vac_values, UserLogin):
    riders_rides['Rider Name'].append(UserLogin.username)
    riders_rides['Origin'].append(origin)
    riders_rides['Destiny'].append(destiny)
    riders_rides['Date'].append(date)
    riders_rides['Time'].append(time)
    riders_rides['Vacancies'].append(vacancies)
    riders_rides['Vacancies Price'].append(vac_values)
    print('Ride registred!')

def ListRides():
    for vagas_disponiveis in riders_rides['Vacancies']:
        if vagas_disponiveis != 0:
            print(f'Vacancies:\n{riders_rides["Vacancies"]}')
            
def Og_Dt_ListRides(origin, destiny):
    for origem in riders_rides['Origin']:
        if origem == origin:
            for destino in riders_rides['Destiny']:
                if destino == destiny:
                    print(f'Founded vacancies:\nOrigin: {riders_rides["Origin"]}\tDestiny: {riders_rides["Destiny"]}')
                    
def ReserveVac(UserLogin.username, UserLogin.useremail):
    index_user = riders_rides['Rider Name'].index(UserLogin.username)
    wished_vac = riders_rides['Vacancies'].index(index_user)
    vac_reserv = int(input('You want reserve vacancie?\n1 - S\t2 - N\n'))
    
    if vac_reserv == 1:
        riders_rides['Vacancies'][wished_vac] -= 1
        print(f'Vacancie reserved!')
        if riders_rides['Vacancies'][wished_vac] == 0:
            print(f'Sorry! Cheio!')
            
def CancelVac(UserLogin.username, UserLogin.useremail):
    index_user = riders_rides['Rider Name'].index(UserLogin.username)
    wished_vac = riders_rides['Vacancies'].index(index_user)
    vac_reserv = int(input('You want cancel the vacancie reserved?\n1 - S\t2 - N\n'))
    
    if vac_reserv == 1:
        riders_rides['Vacancies'][wished_vac] += 1
        print(f'Vacancie reserve canceled!')
        if riders_rides['Vacancies'][wished_vac] == 0:
            print(f'Sorry! Cheio!')
            
def RemoveVac(RideRegister):"""