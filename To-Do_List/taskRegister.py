# I can use a time library for create storage elements with dates
import datetime as dt
import timedelta

"""def taskRegister():
    global generalTasks
    generalTasks = []
    global dictTask
    dictTask = {'Task Name': '', 'Date': ''}
    while True:
        option = 'You want create a task?\nYes\tNo'
        option.lower()
        if option == 'no':
            break
        elif option == 'yes':
            taskName = input('Write your task below:\n')
            taskDate = input()"""
            
variavel = dt.datetime.now()
print(variavel.year)