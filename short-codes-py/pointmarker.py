import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('720x1080')
root.title('Point Marker')
root.resizable = '0, 0'

def add_point1():
    global p1
    num = int(p1['text'])
    num += 1
    p1['text'] = num

def add_point2():
    global p2
    num = int(p2['text'])
    num += 1
    p2['text'] = num

def reset1():
    p1['text'] = '0'

def reset2():
    p2['text'] = '0'
    

while True:
    t1 = tk.Label(root, borderwidth=0,text='Time 1', font='Arial 20').place(x=40, y=30)
    n1 = tk.Entry(root, borderwidth=2, font='Arial 15', justify='center').place(x=20, y=150, width=300, height=100)
    p1 = tk.Label(root, borderwidth=0, width=2, height=2, text='0', font='Arial 40')
    p1.place(x=80, y=300)
    b1 = tk.Button(root, borderwidth=1, text='+ point', font='Arial 15', command=add_point1).place(x=20, y=750, width=300, height=100)
    r1 = tk.Button(root, borderwidth=1, text='reset', font='Arial 15', command=reset1).place(x=20, y=900, width=300, height=100)
    
    t2 = tk.Label(root, borderwidth=0,text='Time 2', font='Arial 20').place(x=420, y=30)
    n2 = tk.Entry(root, borderwidth=2, font='Arial 15', justify='center').place(x=400, y=150, width=300, height=100)
    p2 = tk.Label(root, borderwidth=0, width=2, height=2, text='0', font='Arial 40')
    p2.place(x=450, y=300)
    b2 = tk.Button(root, borderwidth=1, text='+ point', font='Arial 15', command=add_point2).place(x=400, y=750, width=300, height=100)
    r2 = tk.Button(root, borderwidth=1, text='reset', font='Arial 15', command=reset2).place(x=400, y=900, width=300, height=100)
    
    root.mainloop()
