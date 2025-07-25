dictionary = {'nome': []}
for i in range(5):
    dado = input('Insira um nome: ')
    dictionary['nome'].append(dado)
"""print(dictionary)"""

print(f'Coisa: {dictionary["nome"][-1]}')