import os
import shutil

def create_file(path):
    directory = input('Insira o diretório que você quer armazenar o arquivo: ')
    os.chdir(directory)
    try:
        with open(path, 'x') as f:
            f.read(path)
    except PermissionError:
        print('Permissão negada.')
    except TypeError:
        print('O tipo não é permitido.')
        
def create_directory(path):
    directory = input('Insira onde você quer colocar o diretório: ')
    os.chdir(directory)
    try:
        os.mkdir(path)
        print(f'Diretório {path} criado com sucesso!')
    except PermissionError:
        print('Permissão negada.')
    except TypeError:
        print('O tipo não é permitido.')
        
def read_file(path):
    try:
        with open(path, 'r') as f:
            f.read(path)
            print('Arquivo lido com sucesso!')
    except FileNotFoundError or FileExistsError:
        print('Arqiivo não existe')
    except TypeError:
        print('O tipo não é permitido.')
        
def update_file(path, function):
    texto = input('Insira o que você quer atualizar: ')
    try:
        with open(path, function) as f:
            f.write(texto)
            print(f'Arquivo {path} atualizado com sucesso!')
    except FileNotFoundError:
        pass
    except TypeError:
        print('O tipo não é permitido.')

def delete_file(file: str):
    try:
        os.remove(file)
        print(f'Arquivo {file} deletado com sucesso!')
    except FileExistsError or FileNotFoundError:
        print('Arquivo não existe.')
    except TypeError:
        print('O tipo não é permitido.')
        
def delete_directory(path):
    try:
        os.rmdir(path)
        print(f'Diretório {path} removido com sucesso!')
    except TypeError:
        print('O tipo não é permitido.')
        
def fileorganizer(path):
    try:
        files_p = os.listdir(path) # Vai listar todos as pastas dentro do caminho desejado

        for files in files_p:
            f_name, extension = os.path.splitext(files)
            extension = extension[1:]
            
            if os.path.exists(path+'/'+extension):
                shutil.move(path+'/'+files, path+'/'+extension+'/'+files)
                
                print('Succeded operation!')
                print('Your files are organized now!')
            else:
                os.mkdirs(path+'/'+extension) # Cria um diretório
                shutil.move(path+'/'+files, path+'/'+extension+'/'+files)
                
                print('Succeded operation!')
                print('Your files are organized now!')
    except FileNotFoundError:
        print('Caminho não encontrado.')
        
while True:
    options = int(input('1 - Create file\n2 - Create directory\n3 - Read\n4 - Update\n5 - Delete files\n6 - Delete directory\n7 - Organize file\n8 - Exit\n\n'))
    if options == 1:
        file_bacana = input('Insira o nome e extensão do arquivo: ')
        create_file(file_bacana)
    elif options == 2:
        path = input('Insira o nome do diretório que você quer criar: ')
        create_directory(path)
    elif options == 3:
        path = input('Insira o diretório: ')
        read_file(path)
    elif options == 4:
        path = input('Insira o diretório: ')
        option = int(input("Deseja reescrever ou adicionar?\n1 - Reescrever\t2 - Adicionar\n\n"))
        if option == 1:
            update_file(path, function='w')
        elif option == 2:
            update_file(path, function='a')
    elif options == 5:
        path = input('Insira o diretório: ')
        delete_file(path)
    elif options == 6:
        path = input('Insira o diretório: ')
        delete_directory(path)
    elif options == 7:
        path = input('Insira o diretório: ')
        fileorganizer(path)
    elif options == 8:
        exit()