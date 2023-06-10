import tkinter as tk
from time import sleep

def start():
    global ss,s,m,h, root
    if not ss:
        ss = True
        
    while ss:
        if not ss:
            break
        sleep(1)
        s += 1
        if s == 59:
            s = 0
            m += 1
            if m == 59:
                m = 0
                h += 1
        hour['text'] = str(h)
        minute['text'] = str(m)
        second['text'] = str(s)
        root.update()

def pause():
    global ss
    
    ss = False
    
def restart():
    global ss, h, m, s
    if not ss:
        h = m = s = 0
        hour['text'] = '00'
        minute['text'] = '00'
        second['text'] = '00'

root = tk.Tk()
root.rezisable = 0, 0

ss = False


hour = tk.Label(root, text='00', font=("Arial", 20))
hour.place(x=110, y=200)

p1 = tk.Label(root, text=':', font=("Arial", 20))
p1.place(x=245, y=195)

minute = tk.Label(root, text='00', font=("Arial", 20))
minute.place(x=300, y=200)

p2 = tk.Label(root, text=':', font=("Arial", 20))
p2.place(x=435, y=195)

second = tk.Label(root, text='00', font=("Arial", 20))
second.place(x=490, y=200)

start = tk.Button(root, text='start', command=start)
start.place(x=285, y=400)

pause = tk.Button(root, text='pause', command=pause)
pause.place(x=275, y=600)

restart = tk.Button(root, text='restart', command=restart)
restart.place(x=275, y=800)

h = int(hour['text'])
m = int(minute['text'])
s = int(second['text'])

root.mainloop()