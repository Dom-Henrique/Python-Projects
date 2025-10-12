from random import choice

def playerchoice():
    p_choice = input('Choice an option: ').lower
    print(f'Player choice: {p_choice}\n')
    
def cpu_choice(options):
    cpu_choice = choice(options)
    print(f'CPU choice: {cpu_choice}\n')