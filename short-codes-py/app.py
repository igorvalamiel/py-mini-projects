import tkinter as tk
from time import sleep

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        def home():
            title1 = tk.Label(self, text='Study', font='Arial 32')
            title1.place(x=200, y=20)
            title2 = tk.Label(self, text='Helper', font='Arial 32')
            title2.place(x=180, y=180)

            
            bmath = tk.Button(self, text='Matemática', width=10, heigh=1, font='Arial 10', bg='#00CC88', fg='#EEEEEE', border=5, command=lambda:movebut(bmath, 200, 380))
            bmath.place(x=200, y=380)
            bbio = tk.Button(self, text='Biologia', width=10, heigh=1, font='Arial 10', bg='#00CC88', fg='#EEEEEE', border=5, command=lambda:movebut(bbio, 200, 495))
            bbio.place(x=200, y=495)
            bquim = tk.Button(self, text='Química', width=10, heigh=1, font='Arial 10', bg='#00CC88', fg='#EEEEEE', border=5, command=lambda:movebut(bquim, 200, 610))
            bquim.place(x=200, y=610)
            bfisc = tk.Button(self, text='Física', width=10, heigh=1, font='Arial 10', bg='#00CC88', fg='#EEEEEE', border=5, command=lambda:movebut(bfisc, 200, 725))
            bfisc.place(x=200, y=725)
            bgeo = tk.Button(self, text='Geografia', width=10, heigh=1, font='Arial 10', bg='#00CC88', fg='#EEEEEE', border=5, command=lambda:movebut(bgeo, 200, 840))
            bgeo.place(x=200, y=840)
            bhist = tk.Button(self, text='História', width=10, heigh=1, font='Arial 10', bg='#00CC88', fg='#EEEEEE', border=5, command=lambda:movebut(bhist, 200, 955))
            bhist.place(x=200, y=955)
            bother = tk.Button(self, text='Outros', width=10, heigh=1, font='Arial 10', bg='#00CC88', fg='#EEEEEE', border=5, command=lambda:movebut(bother, 200, 1070))
            bother.place(x=200, y=1070)
        
            self.blist = [bmath, bbio, bquim, bfisc, bgeo, bhist, bother]    
        home()
        
        def movebut(btn, posx, posy, bl=self.blist):
            passo = float(posy/posx)
            pxi = posx
            pyi = posy
            while pxi != 0:
                if pxi > 0:
                    pxi -= 1
                elif pxi < 0:
                    pxi += 1
                if pyi > 0:
                    pyi -= passo
                elif pyi < 0:
                    pyi += passo
                btn.place(x=pxi, y=pyi)
                sleep(0.001)
                btn.update()
            for elem in bl:
                if elem != btn:
                    elem.place_forget()
            

root = Root()
root.mainloop()