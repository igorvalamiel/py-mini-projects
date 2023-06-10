import tkinter as tk
from random import choice

def ch():
    xl = list(range(0, 501))
    yl = list(range(0, 1101))
    x = choice(xl)
    y = choice(yl)
    return x, y

def ct():
    global txt
    txt['text'] = 'É... eu sabia.'
    
def cp():
    global no
    xp, yp = ch()
    no.place(x=xp, y=yp)

root = tk.Tk()

txt = tk.Label(root, text='Você é Humilde?')
txt.place(x=260, y=300)

yes = tk.Button(root, text='Não', width=8, height=2, command=ct)
yes.place(x=250, y=600)

no = tk.Button(root, text='Sim', width=8, height=2, command=cp)
no.place(x=250, y=800)

root.mainloop()