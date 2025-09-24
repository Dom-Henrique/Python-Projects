# Usuário insere a URL em formato texto
# Função pega a URL e retira os espaços indesejados

url = input('URL: ')
url = url.removeprefix('https://')
new_url = ''

for i in url:
    new_url += i
    if i == '/':
        break
    
print(f'New URL: {new_url}')

# Ele vai retornar a URL padrão caso ele esteja em algo mais específico.
# Exemplo: se o link for de um vídeo no YouTube, ele vai retornar ao menu principal.