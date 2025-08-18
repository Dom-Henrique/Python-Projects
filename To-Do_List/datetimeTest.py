import datetime as dt
from datetime import timedelta

datinha = dt.datetime(day = 12, month = 12, year = 1912)
lista = []

datinha = datinha.strftime(f'%d/%m/%Y')

print(datinha)