import tkinter as tk

root = tk.Tk()
root.configure(bg='#333333')

def change():
    global onoff, root
    
    text = onoff['text']
    
    if text == 'on':
        onoff.configure(text='off', bg='#333333', fg='#DDDDDD')
        root.configure(bg='#DDDDDD')
    elif text == 'off':
        onoff.configure(text='on', bg='#DDDDDD', fg='#333333')
        root.configure(bg='#333333')

def dst():
    global dest, onoff
    dest.destroy()
    onoff.destroy()
    
def rst():
    global root, dest, onoff, change(), dst()
    
    color = root['bg']
    if color == '#333333':
        onoff = tk.Button(root, borderwidth=0, bg='#DDDDDD', text='on', font='Arial 16', width=3, heigh=2, command=change)
        onoff.place(x=250, y=100)
    elif color = '#DDDDDD':
        onoff = tk.Button(root, borderwidth=0, bg='#333333', text='off', font='Arial 16', width=3, heigh=2, command=change)
        onoff.place(x=250, y=100)
    dest = tk.Button(root, borderwidth=0, bg='#DDDDDD', text='destroy', font='Arial 16', width=5, heigh=2, command=dst)
    dest.place(x=215, y=400)

voltar = ''
onoff = ''

onoff = tk.Button(root, borderwidth=0, bg='#DDDDDD', text='on', font='Arial 16', width=3, heigh=2, command=change)
onoff.place(x=250, y=100)

dest = tk.Button(root, borderwidth=0, bg='#DDDDDD', text='destroy', font='Arial 16', width=5, heigh=2, command=dst)
dest.place(x=215, y=400)

voltar = tk.Button(root, borderwidth=0, bg='#DDDDDD', text='voltar', font='Arial 16', width=5, heigh=2, command=rst)
voltar.place(x=215, y=700)

root.mainloop()