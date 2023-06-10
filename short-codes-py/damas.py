import tkinter as tk

root = tk.Tk()

def block(posy, initcolor):
    color = initcolor
    posx = 0
    for i in range(8):
        b = tk.Button(root, bg=color, width=2, height=2)
        b.place(x=posx, y=posy)
        posx += 90
        if color == 'black':
            color = 'white'
        else:
            color = 'black'

while True:
    posy = 300
    color = 'black'
    for i in range(8):
        block(posy, color)
        posy += 95
        if color == 'black':
            color = 'white'
        else:
            color = 'black'
    root.mainloop()