# I can use a time library for create storage elements with dates
import datetime as dt
from datetime import timedelta

def taskRegister():
    global generalTasks
    generalTasks = []
    global dictTask
    dictTask = {'Task Name': '', 'Date': ''}
    while True:
        option = input('You want create a task?\nYes\tNo\n').lower()
        if option == 'no':
            break
        elif option == 'yes':
            taskName = input('Write your task below:\n')
            taskDate = input('Choose a date:\n')
            formatDate = f'%d%m%Y'
            Datinha = dt.strptime(taskDate, formatDate)
            print(f'Task create!\n\
                Task: {taskName}\n \
                Date: {Datinha}')
            
taskRegister()