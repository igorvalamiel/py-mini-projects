import tkinter as tk
from tkinter import ttk
from time import sleep

root = tk.Tk()
root.geometry("800x300")
root.configure(background='black')

def start():
    global root, inp, texto
    texto = inp.get()
    for ele in root.winfo_children(): ele.destroy()
    
texto = ''

txt = tk.Label(root, text="Digite a frase aqui:", font='Arial 20', bg='black', fg='white')
txt.place(x=280, y=80)
inp = tk.Entry(root, width=46, font='Arial 20')
inp.place(x=50, y=130)
btn = tk.Button(root, text='Começar', width=10, font='Arial 20', command=lambda:start())
btn.place(x=320, y=200)

if texto != '':
    novo_txt = tk.Label(root, text=texto, font='Arial 20', bg='black', fg='white')
    txt.place(x=0, y=0)

root.mainloop()
