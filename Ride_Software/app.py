# Projeto BlaBlaCar

# Usuários podem pedir ou oferecer carona;
# Não utilizar funções e bibliotecas

# P1 - Registro de usuário
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
user_data = {'name_user': [], 'email_user': [], 'password_user': []}
rides_data = {'origem': [], 'data': [], 'horario': [], 'vagas': [], 'valor_vaga': [], 'dono': []}
while True:
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
        print('Usuário cadastrado com sucesso!')
        print('Faça o seu login')
        continue
        
    elif (decision == 2):
        print('#'*50)
        print('OPÇÃO ESCOLHIDA:\n2 - Logar')
        nome_usuario = input('Insira o nome de usuário:\n')
        email_usuario = input('Insira um e-mail válido:\n')
        senha_usuario = input('Insira uma senha:\n')
        if (nome_usuario in user_data):
            if (email_usuario in user_data):
                if (senha_usuario in user_data):
                    print('Login bem-sucedido!')
                else:
                    print('[ERRO]\nUsuário não cadastrado!')
                    
        while True:
            print('#'*50)
            print(f'Bem-vindo, {nome_usuario}!')
            login_out = input('Deseja fazer logout?\nS\tN\n')
            if (login_out == 's' or login_out == 'S'):
                print('Login desfeito.')
                exit()
            if (login_out == 'n' or login_out == 'N'):
                print('#'*50)
                options = int(input('Escolha uma das opções abaixo:\n\t \
                    1 - Cadastrar caronas\n \
                    2 - Listar caronas disponíveis\n \
                    3 - Buscar carona por origem e destino\n \
                    4 - Reservar vaga\n'))
                if (options == 1):
                    print('#'*50)
                    print('OPÇÃO ESCOLHIDA:\n1 - Cadastrar caronas')
                    origem_carona = input('Local de origem:\n')
                    rides_data['origem'].append(origem_carona)
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

                    print('Cadastro feito com sucesso!')
                    print(f'Origem: {rides_data["origem"][-1]}\n \
                        Data: {rides_data["data"][-1]}\n \
                        Horário: {rides_data["horario"][-1]}\n \
                        Vagas: {rides_data["vagas"][-1]}\n \
                        Valor por vaga: {rides_data["valor_vaga"][-1]}\n \
                        Motorista: {rides_data["dono"][-1]}')
                    print(rides_data)
                    
                    cancel_ride = input('Deseja cancelar a carona?\n\n[ESSA AÇÃO NÃO PODE SER DESFEITA]')
                    if (cancel_ride == 's' or cancel_ride == 'S'):
                        rides_data.clear()
                        print('Carona cancelada!')
                    elif (cancel_ride == 'n' or cancel_ride == 'N'):
                        continue
                elif (options == 2):
                    print('#'*50)
                    print('OPÇÃO ESCOLHIDA:\n2 - Listar caronas disponíveis')
                    
    #                5 - Cancelar reserva\n \
    #                6 - Remover carona\n)
                # Reservar vaga -> Caronas disponíveis
                # Cancelar reserva -> Reservar vaga
                # Cancelar carona -> Cadastrar caronas (OK)
                # Detalhes da carona -> Caronas disponíveis
                # Remover carona -> Detalhes da carona