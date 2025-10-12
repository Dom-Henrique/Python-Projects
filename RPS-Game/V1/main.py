# Creating an rock, paper and scissor game with built-in functions
from random import choice
from modules import *
import time

options = ['rock', 'paper', 'scissor']

print('WELCOME TO THE\nROCK, PAPER AND SCISSOR GAME!')

username = input('Username: ')

try:
    game_time = int(input('Choice an time (more than 1 minute): '))
    print(f'Time defined to {game_time} minutes')
except TypeError:
    print('Invalid type input.')

player_score = 0
cpu_score = 0

while True:
    pc = playerchoice()
    cc = cpu_choice(options)
    
    if pc in options:
        # Empate
        if pc == cc:
            pass
        # Jogador
        elif pc == 'rock' and cc == 'scissor':
            player_score += 1
        elif pc == 'paper' and cc == 'rock':
            player_score += 1
        elif pc == 'scissor' and cc == 'paper':
            player_score += 1
        # CPU
        elif cc == 'rock' and pc == 'scissor':
            cpu_score += 1
        elif cc == 'paper' and pc == 'rock':
            cpu_score += 1
        elif cc == 'scissor' and pc == 'paper':
            cpu_score += 1
    
    game_time -= 1
    time.sleep(1)
    
    if game_time == 0:
        print('GAME OVER!')
        if player_score > cpu_score:
            print(f'Winner: {username}\nScore: {player_score}')
        elif player_score < cpu_score:
            print(f'Winner: CPU\nScore: {cpu_score}')