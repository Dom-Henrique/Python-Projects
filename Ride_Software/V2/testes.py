lista = []

# Tenho que adicionar um dicionário para cada usuário COM AS INFORMAÇÕES DELE
for i in range(1, 5):
    dicionario = {'Nome': '', 'Idade': '', 'Endereço': ''}
    name = input('Insert your name: ')
    age = int(input('Insert your age: '))
    adress = input('Insert your adress: ')
    print('*'*50)
    dicionario['Nome'] = name
    dicionario['Idade'] = age
    dicionario['Endereço'] = adress
    lista.append(dicionario)
    
print(lista)