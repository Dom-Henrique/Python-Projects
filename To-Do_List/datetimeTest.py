import datetime as dt
from datetime import timedelta # 'timedelta' is a module from 'datetime'
import zoneinfo as zif

aniversariodoDom = '29/12/2006'
"""dianiverdoDom = 'Sex'"""

aniversariodoDom = dt.datetime.strptime(aniversariodoDom, f'%d/%m/%Y')
"""dianiverdoDom = dt.datetime.strptime(dianiverdoDom, f'%a')"""
print(aniversariodoDom)
"""print(dianiverdoDom)"""
# Precisa estar sempre condizente com a variável

niverKiddao = dt.datetime(day = 5, month = 4, year = 2006)

print(niverKiddao.strftime(f'%d/%m/%Y'))
print(niverKiddao.strftime(f'%A'))

zoneinfo = zif.ZoneInfo('America/Sao_Paulo')

niverKiddao_SP = niverKiddao.astimezone(zoneinfo)

print(niverKiddao_SP)