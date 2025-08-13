# Create a "To Do List"

from userLogin import *
from userRegister import *
from taskRegister import *

# Apresentação do sistema
print('*'*50)
print('Program initializated')
print('*'*50)

print('Welcome!')

print('Please, log in the sistem or register new user')
while True:
    print('#'*50)
    decision = int(input('1 - Login\t2 - User Register\n'))
    if decision == 1:
        userLogin()
        break
    elif decision == 2:
        userRegister()
        break
    else:
        print('Please, try again\n')