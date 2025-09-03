# Quiz about Python
from functions import *

print('*'*50)
print('PYTHON QUIZ')
print('*'*50)

score = 0

score = Question1(score) # Atribuir a variável desejada a função faz com que ela assuma o valor da última 
score = Question2(score)
score = Question3(score)

print(f'Score: {score}')