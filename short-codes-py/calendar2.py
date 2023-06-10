import tkinter as tk
import datetime as dt
import calendar as cal

#date part

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

#tkinter part
root = tk.Tk()
root.geometry('720x1232')

d, w, m, y = get_date()

days = 31

if m == 'Fevereiro':
    if cal.isleap(y):
        days = 29
    else:
        days = 28
elif m in ['Janeiro', 'Março', 'Maio', 'Julho', 'Agosto', 'Outubro', 'Dezembro']:
    days = 31
elif m in ['Abril', 'Junho', 'Setembro', 'Novembro']:
    days = 30

def Table():
    global datew, dateh, days
    
    posx = 0
    posy = 300
    
    while True:
        for j in range(0,7):
            d = tk.Label(root, width=0, height=2, borderwidth=1, text='01', font='Arial 20', highlightthickness=4,  highlightbackground='#000000')
            d.place(x=posx, y=posy)
            posx+=100
            days -= 1
            if days == 0:
                break
        posx = 0
        posy+=180
        if days == 0:
            break
        
Table()
root.mainloop()