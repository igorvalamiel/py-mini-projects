import tkinter as tk

def write(x):
    global screen
    slist = ['+', '-', '÷', '×', '√', '^']
    nlist = ['0', '1', '2', '3', '4', '5', '6' ,'7', '8' ,'9']
    value = screen.get()
    if x in slist:
        if value == '':
            pass
        else:
            if value[-1] not in slist:
                screen.insert(tk.END, x)
            elif value[-1] in slist:
                delete()
                screen.insert(tk.END, x)
            else:
                pass
    else:
        if x == '%':
            if value == '':
                pass
            else:
                if value[-1] == '%':
                    delete()
        if x == '(':
            if value == '':
                pass
            else:
                if value[-1] == ')':
                    screen.insert(tk.END, '×(')
                    delete()
                else:
                    screen.insert(tk.END, x)
                    delete()
        if x == '.':
            if value == '':
                screen.insert(tk.END, '0.')
            elif value[-1] not in nlist:
                screen.insert(tk.END, '0.')
            else:
                screen.insert(tk.END, '.')
        else:    
            screen.insert(tk.END, x)
    
def clear():
    global screen
    screen.delete(0, tk.END)
    
def delete():
    global screen
    value = screen.get()
    n = len(value)
    screen.delete(n-1, tk.END)
    
def mm():
    global screen
    value = screen.get()
    if value == '':
        screen.insert(0, '-')
    else:
        if value[0] == '-':
            screen.delete(0, 1)
            screen.insert(0, '+')
        elif value[0] == '+':
            screen.delete(0, 1)
            screen.insert(0, '-')
        else:
            screen.insert(0, '-')
    
def equal():
    global screen
    value = screen.get()
    nv = ''
    raiz = False
    for a in value:
        if a == '^':
            nv += '**'
        elif a == '√':
            raiz = True
        elif a == '÷':
            nv += '/'
        elif a == '×':
            nv += '*'
        elif a == '%':
            nv += '/100'
        else:
            if raiz:
                if a == ')':
                    nv += '**0.5'
                    raiz = False
                else:
                    pass
            nv += a
    for i in list(range(0, 10)):
        s0 = str(i) + '/0'
        if s0 in nv:
            clear()
            screen.insert(0, 'Erro')
    if '/0' not in nv:
        res = str(eval(nv))
        clear()
        screen.insert(0, res)
            

root = tk.Tk()
root.title('Calculator')
root.rezisable = 0, 0

screen = tk.Entry(root, justify='right', font=("Arial", 25))
screen.place(x=0, y=0)
screen.pack(fill=tk.X, ipady=125)

bc = tk.Button(root, width=4, height=2, text='C', borderwidth=2, font=("Arial", 10), fg='#f90', command=lambda:clear())
bc.place(x=7.5, y=390)

bp1 = tk.Button(root, width=4, height=2, text='(', borderwidth=2, font=("Arial", 10), command=lambda:write('('))
bp1.place(x=185, y=390)

bp2 = tk.Button(root, width=4, height=2, text=')', borderwidth=2, font=("Arial", 10), command=lambda:write(')'))
bp2.place(x=362, y=390)

bspc = tk.Button(root, width=4, height=2, text='⌫', borderwidth=2, font=("Arial", 10), fg='#f00', command=lambda:delete())
bspc.place(x=540, y=390)


bpc = tk.Button(root, width=4, height=2, text='%', borderwidth=2, font=("Arial", 10), command=lambda:write('%'))
bpc.place(x=7.5, y=530)

bpot = tk.Button(root, width=4, height=2, text='xʸ', borderwidth=2, font=("Arial", 10), command=lambda:write('^'))
bpot.place(x=185, y=530)

brad = tk.Button(root, width=4, height=2, text='√', borderwidth=2, font=("Arial", 10), command=lambda:write('√('))
brad.place(x=362, y=530)

bdiv = tk.Button(root, width=4, height=2, text='÷', borderwidth=2, font=("Arial", 10), command=lambda:write('÷'))
bdiv.place(x=540, y=530)


b7 = tk.Button(root, width=4, height=2, text='7', borderwidth=2, font=("Arial", 10), command=lambda:write('7'))
b7.place(x=7.5, y=670)

b8 = tk.Button(root, width=4, height=2, text='8', borderwidth=2, font=("Arial", 10), command=lambda:write('8'))
b8.place(x=185, y=670)

b9 = tk.Button(root, width=4, height=2, text='9', borderwidth=2, font=("Arial", 10), command=lambda:write('9'))
b9.place(x=362, y=670)

bmult = tk.Button(root, width=4, height=2, text='×', borderwidth=2, font=("Arial", 10), command=lambda:write('×'))
bmult.place(x=540, y=670)


b4 = tk.Button(root, width=4, height=2, text='4', borderwidth=2, font=("Arial", 10), command=lambda:write('4'))
b4.place(x=7.5, y=810)

b5 = tk.Button(root, width=4, height=2, text='5', borderwidth=2, font=("Arial", 10), command=lambda:write('5'))
b5.place(x=185, y=810)

b6 = tk.Button(root, width=4, height=2, text='6', borderwidth=2, font=("Arial", 10), command=lambda:write('6'))
b6.place(x=362, y=810)

bmin = tk.Button(root, width=4, height=2, text='-', borderwidth=2, font=("Arial", 10), command=lambda:write('-'))
bmin.place(x=540, y=810)


b1 = tk.Button(root, width=4, height=2, text='1', borderwidth=2, font=("Arial", 10), command=lambda:write('1'))
b1.place(x=7.5, y=950)

b2 = tk.Button(root, width=4, height=2, text='2', borderwidth=2, font=("Arial", 10), command=lambda:write('2'))
b2.place(x=185, y=950)

b3 = tk.Button(root, width=4, height=2, text='3', borderwidth=2, font=("Arial", 10), command=lambda:write('3'))
b3.place(x=362, y=950)

bmais = tk.Button(root, width=4, height=2, text='+', borderwidth=2, font=("Arial", 10), command=lambda:write('+'))
bmais.place(x=540, y=950)


bmn = tk.Button(root, width=4, height=2, text='±', borderwidth=2, font=("Arial", 10), command=lambda:mm())
bmn.place(x=7.5, y=1090)

b0 = tk.Button(root, width=4, height=2, text='0', borderwidth=2, font=("Arial", 10), command=lambda:write('0'))
b0.place(x=185, y=1090)

bp = tk.Button(root, width=4, height=2, text='.', borderwidth=2, font=("Arial", 10), command=lambda:write('.'))
bp.place(x=362, y=1090)

bequal = tk.Button(root, width=4, height=2, text='=', borderwidth=2, font=("Arial", 10), command=lambda:equal())
bequal.place(x=540, y=1090)

root.mainloop()