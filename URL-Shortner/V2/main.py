import pyshorteners

s = pyshorteners.Shortener() # Cria um objeto que especifica o que queremos fazer

url = input('URL: ')

new_url = s.tinyurl.short(url)

print(f'URL: {url}\nShorted URL: {new_url}')