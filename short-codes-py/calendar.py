import datetime as dt

def mname(m):
    mn = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return mn[m-1]

def wname(w):
    wn = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    return wn[w-1]

year = dt.date.today().year
month = dt.date.today().month
day = dt.date.today().day
week = dt.date.today().weekday()

month = mname(month)
week = wname(week)

def get_date():
    return day, week, month, year

d, w, m, y = get_date()

print(f'{d} de {m} de {y}, {w}')