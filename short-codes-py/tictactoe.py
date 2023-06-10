import tkinter as tk

root = tk.Tk()
root.geometry('720x1080')
root.title('Tic-Tac-Toe')
opc = 0
l = '000000000'

def drawx(posx=0, posy=0):
    global root
    x = tk.Label(root, text='x', font='Arial 40').place(x=10+posx, y=10+posy, width=180, height=180)
    
def drawo(posx=0, posy=0):
    global root
    o = tk.Label(root, text='o', font='Arial 40').place(x=10+posx, y=10+posy, width=180, height=180)

def choice(posx, posy, pos):
    global opc, l
    if opc == 1:
        drawx(posx, posy)
        l.replace(l[pos], '1')
    if opc == 2:
        drawo(posx, posy)
        l.replace(l[pos], '2')
        
def cx():
    global opc
    opc = 1

def co():
    global opc
    opc = 2
    
def reset():
    pass
    
def change_text(self, new_text):
    s = tk.Label(self)
    s.configure(text=str(new_text))

while True:
    
    bx = tk.Button(root, bg='red', text='x', font='Arial 20', borderwidth=3, command=lambda:cx()).place(x=100, y=1040, width=100, height=150)
    
    bo = tk.Button(root, bg='blue', text='o', font='Arial 20', borderwidth=3, command=lambda:co()).place(x=500, y=1040, width=100, height=150)
    
    rs = tk.Button(root, text='reset', font='Arial 20', borderwidth=3, command=lambda:reset()).place(x=225, y=1070, width=250, height=100)
    
    py1, py2, py3 = 400, 600, 800
    px1, px2, px3 = 50, 250, 450
    s1 = tk.Button(root, borderwidth=3, command=lambda:choice(px1, py1, 0)).place(x=px1, y=py1, width=200, height=200)
    s2 = tk.Button(root, borderwidth=3, command=lambda:choice(px2, py1, 1)).place(x=px2, y=py1, width=200, height=200)
    s3 = tk.Button(root, borderwidth=3, command=lambda:choice(px3, py1,2)).place(x=px3, y=py1, width=200, height=200)
    
    s4 = tk.Button(root, borderwidth=3, command=lambda:choice(px1, py2, 3)).place(x=px1, y=py2, width=200, height=200)
    s5 = tk.Button(root, borderwidth=3, command=lambda:choice(px2, py2, 4)).place(x=px2, y=py2, width=200, height=200)
    s6 = tk.Button(root, borderwidth=3, command=lambda:choice(px3, py2, 5)).place(x=px3, y=py2, width=200, height=200)
    
    s7 = tk.Button(root, borderwidth=3, command=lambda:choice(px1, py3, 6)).place(x=px1, y=py3, width=200, height=200)
    s8 = tk.Button(root, borderwidth=3, command=lambda:choice(px2, py3, 7)).place(x=px2, y=py3, width=200, height=200)
    s9 = tk.Button(root, borderwidth=3, command=lambda:choice(px3, py3, 8)).place(x=px3, y=py3, width=200, height=200)
    
    win = tk.Label(root, text='', font='Arial 20').place(x=110, y=150, width=500, height=100)
    
    winx = 'X Ganhou!'
    wino = 'O Ganhou!'
    
    if l[0] == l[1] == l[2]:
       change_text(win, winx)
    
    root.mainloop()
