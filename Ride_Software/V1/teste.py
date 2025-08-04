from random import randint

dicionario = {'nome': [], 'id_vaga': []}
i = 0
while i < 5:
    nome = input('seila:\n')
    dicionario['nome'].append(nome)
    dicionario['id_vaga'].append(randint(1000000000, 9999999999))
    i += 1
print(f'{dicionario['nome']}')