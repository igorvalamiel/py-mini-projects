import tkinter as tk
import pygame as pg

root = tk.Tk()

def close():
    root.quit()
    
def word(x):
    return x

root.geometry('300x300')
root.title("Palavra")
root.resizable = 0, 0

t = tk.Label(root, text='Digite a palavra aqui:', font='Arial 16')
t.pack(padx = 20, pady=60)

a = tk.Entry(root, borderwidth=1, font = 'Arial 32')
a.pack(padx=0, pady=150, ipadx=30, ipady=50)

b = tk.Button(root, text="Enviar", font = 'Arial 20', command=close)
b.pack(padx = 140, pady=150, ipadx=20, ipady=15)

root.mainloop()
