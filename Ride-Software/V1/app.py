# Projeto BlaBlaCar

# Usuários podem pedir ou oferecer carona;
# Não utilizar funções e bibliotecas

# P1 - Registro de usuário
from random import randint
print("""
        ______
       /|_||_\\`.__
      (   _    _ _\\
______=`-(_)--(_)-'___________________________________________________________________

██████╗ ██╗      █████╗ ██████╗ ██╗      █████╗  ██████╗ █████╗ ██████╗ 
██╔══██╗██║     ██╔══██╗██╔══██╗██║     ██╔══██╗██╔════╝██╔══██╗██╔══██╗
██████╔╝██║     ███████║██████╔╝██║     ███████║██║     ███████║██████╔╝
██╔══██╗██║     ██╔══██║██╔══██╗██║     ██╔══██║██║     ██╔══██║██╔══██╗
██████╔╝███████╗██║  ██║██████╔╝███████╗██║  ██║╚██████╗██║  ██║██║  ██║
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
""")

print('BEM-VINDO AO BLABLACAR!')
user_data = {'name_user': [], 'email_user': [], 'password_user': [], 'type_user': []}
rides_data = {'origem': [], 'destino': [], 'data': [], 'horario': [], 'vagas': [], 'valor_vaga': [], 'dono': [], 'id_vaga': []}
while True:
    print('#'*50)
    decision = int(input('Escolha uma opção abaixo:\n \
        1 - Cadastrar usuário\n \
        2 - Logar\n'))
    if (decision == 1):
        print('#'*50)
        print('OPÇÃO ESCOLHIDA:\n1 - Cadastrar usuário')
        nome_usuario = input('Insira o nome de usuário:\n')
        user_data['name_user'].append(nome_usuario)
        while True:
            email_usuario = input('Insira um e-mail válido:\n')
            if ('@' and '.com' in email_usuario):
                user_data['email_user'].append(email_usuario)
                break
            else:
                print('E-mail inválido!')
                continue
        senha_usuario = input('Insira uma senha:\n')
        user_data['password_user'].append(senha_usuario)
        tipo_usuario = int(input('Qual tipo melhor define você?\n1 - Motorista\t2 - Passageiro\n'))
        user_data['type_user'].append(tipo_usuario)
        print('Usuário cadastrado com sucesso!')
        print('Faça o seu login')
        continue
        
    elif (decision == 2):
        print('#'*50)
        print('OPÇÃO ESCOLHIDA:\n2 - Logar')
        nome_usuario = input('Insira o nome de usuário:\n')
        email_usuario = input('Insira um e-mail válido:\n')
        senha_usuario = input('Insira uma senha:\n')
        
        if (nome_usuario in user_data['name_user']):
            if (email_usuario in user_data['email_user']):
                if (senha_usuario in user_data['password_user']):
                    print('Login bem-sucedido!')
                    print(f'Tipo de cadastro: {user_data["type_user"]}')
                else:
                    print('[ERRO]\nUsuário não cadastrado!')
                    continue
                    
        while True:
            print('#'*50)
            print(f'Bem-vindo, {nome_usuario}!')
            login_out = input('Deseja fazer logout?\nS\tN\n')
            if (login_out == 's' or login_out == 'S'):
                print('Login desfeito.')
                break # Vai interromper esse laço de repetição
            if (login_out == 'n' or login_out == 'N'):
                print('#'*50)
                options = int(input('Escolha uma das opções abaixo:\n \
                    1 - Cadastrar caronas\n \
                    2 - Listar caronas disponíveis\n \
                    3 - Buscar carona por origem e destino\n \
                    4 - Reservar vaga\n'))
                if (options == 1 and user_data['type_user'] == 1):
                    print('#'*50)
                    print('OPÇÃO ESCOLHIDA:\n1 - Cadastrar caronas')
                    origem_carona = input('Local de origem:\n')
                    rides_data['origem'].append(origem_carona)
                    destino_carona = input('Local de destino:\n')
                    rides_data['destino'].append(destino_carona)
                    rides_time = input('Data:\n')
                    rides_data['data'].append(rides_time)
                    rides_hour = input('Horário:\n')
                    rides_data['horario'].append(rides_hour)
                    rides_vacancies = int(input('Número de vagas:\n'))
                    rides_data['vagas'].append(rides_vacancies)
                    # O tamanho da lista poderia ter o limite inserido pelo usuário
                    rides_data['vagas']
                    rides_vacancies_value = float(input('Valor por vaga:\n'))
                    rides_data['valor_vaga'].append(rides_vacancies_value)
                    rides_data['dono'] = user_data['name_user']
                    rides_data['id_vaga'] = randint(1000000, 9999999)

                    print('Cadastro feito com sucesso!')
                    print(f'Origem: {rides_data["origem"][-1]}\n \
                        Destino: {rides_data["destino"]}\n \
                        Data: {rides_data["data"][-1]}\n \
                        Horário: {rides_data["horario"][-1]}\n \
                        Vagas: {rides_data["vagas"][-1]}\n \
                        Valor por vaga: {rides_data["valor_vaga"][-1]}\n \
                        Motorista: {rides_data["dono"][-1]}\n \
                        ID: {rides_data["id_vaga"][-1]}')
                    """print(rides_data)"""
                    
                    cancel_ride = input('Deseja cancelar a carona?\n\n[ESSA AÇÃO NÃO PODE SER DESFEITA]')
                    if (cancel_ride == 's' or cancel_ride == 'S'):
                        rides_data.pop()
                        print('Carona cancelada!')
                    elif (cancel_ride == 'n' or cancel_ride == 'N'):
                        continue
                elif (options == 1 and user_data['type_user'] != 1):
                    print('OPÇÃO INDISPONÍVEL!')
                    continue
                elif (options == 2):
                    print('#'*50)
                    print('OPÇÃO ESCOLHIDA:\n2 - Listar caronas disponíveis')
                    print(f'Caronas disponíveis: {rides_data['dono'], rides_data["id_vaga"]}')
                    print(f'Vagas disponíveis: {rides_data["vagas"]}')
                    reservar_vaga = input('Deseja reservar vaga?\nS\tN\n')
                    if (reservar_vaga == 'S' or reservar_vaga == 's'):
                        id_ride = int(input('Insira o ID: '))
                        if (id_ride in rides_data['id_vaga']):
                            rides_data['vagas'] -= 1
                            if (rides_data['vagas'] == 0):
                                print('Carona lotada!')
                    elif (reservar_vaga == 'N' or reservar_vaga == 'n'):
                        continue
                elif (options == 3):
                    print('#'*50)
                    print('OPÇÃO ESCOLHIDA:\n3 - Buscar carona por origem e destino')
                    while True:
                        search_ride = input('Insira o local de onde você deseja partir: ')
                        if (search_ride in rides_data['origem']):
                            print(f'Vagas disponíveis:\n{rides_data["origem"]}')
                            break
                        elif (search_ride not in rides_data['origem']):
                            print(f'[ERRO]\nTENTE NOVAMENTE')
                            continue
                elif (options == 4):
                    print('#'*50)
                    print('OPÇÃO ESCOLHIDA:\n4 - Reservar vag')
                    reservar_vaga = input('Deseja reservar vaga?\nS\tN\n')
                    if (reservar_vaga == 'S' or reservar_vaga == 's'):
                        id_ride = int(input('Insira o ID: '))
                        if (id_ride in rides_data['id_vaga']):
                            rides_data['vagas'] -= 1
                            if (rides_data['vagas'] == 0):
                                print('Carona lotada!')
                    elif (reservar_vaga == 'N' or reservar_vaga == 'n'):
                        continue
                    
                    
    #                5 - Cancelar reserva\n \
    #                6 - Remover carona\n)
                # Reservar vaga -> Caronas disponíveis
                # Cancelar reserva -> Reservar vaga
                # Cancelar carona -> Cadastrar caronas (OK)
                # Detalhes da carona -> Caronas disponíveis
                # Remover carona -> Detalhes da carona