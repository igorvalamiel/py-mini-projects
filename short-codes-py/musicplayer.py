import tkinter as tk
import pygame as pg

pg.init()

root = tk.Tk()
root.geometry('350x500')
root.title('Calculator')
root.resizable = (0, 0)

def JB():
    pg.mixer.music.load("/storage/emulated/0/Download/Justin_Bieber_Sorry_VERSÃO_PAGODE.mp3")
    pg.mixer.music.play()

def AD():
    pg.mixer.music.load("/storage/emulated/0/Download/Adele_Easy_On_Me_Nilwan_BREGA_FUNK_Remix_.mp3")
    pg.mixer.music.play()
    
def DC():
    pg.mixer.music.load("/storage/emulated/0/Download/Doja_Cat_Woman_FUNK_RAVE_Funk_Remix.mp3")
    pg.mixer.music.play()
    
def DL():
    pg.mixer.music.load("/storage/emulated/0/Download/Yan_Pablo_DJ_e_Dua_Lipa_IDGAF_FUNK_REMIX_.mp3")
    pg.mixer.music.play(start=10)
    
def BE():
    pg.mixer.music.load("/storage/emulated/0/Download/Yan_Pablo_DJ_e_Billie_Eilish_bad_guy_FUNK_REMIX.mp3")
    pg.mixer.music.play()
    
def RI():
    pg.mixer.music.load("/storage/emulated/0/Download/RIHANNA_UMBRELLA_VERSÃO_SAFADÃO.mp3")
    pg.mixer.music.play()
    
def FH():
    pg.mixer.music.load("/storage/emulated/0/Samsung/Music/Yan_Pablo_DJ_feat_Fifth_Harmony_e_Kid_Ink_Worth.mp3")
    pg.mixer.music.play(start=4)

def OD():
    pg.mixer.music.load("/storage/emulated/0/Samsung/Music/One Direction - No Control FUNK REMIX - Mathuga Beats.mp3")
    pg.mixer.music.play()
    
def pa():
    pg.mixer.music.pause()  
    
def up():
    pg.mixer.music.unpause()
 
while True:
    
    txt = tk.Label(root, text='Clique para ouvir:', font='Arial 14')
    txt.place(x=120, y=50, width=500, height=100)
    
    
    b1 = tk.Button(root, borderwidth=1, text='Justin Bieber',  font='Arial 12', command=lambda:JB())
    b1.place(x=190, y=200, width=350, height=100)
    
    b2 = tk.Button(root, borderwidth=1, text='Adele',  font='Arial 12', command=lambda:AD())
    b2.place(x=190, y=300, width=350, height=100)
    
    b3 = tk.Button(root, borderwidth=1, text='Doja Cat',  font='Arial 12', command=lambda:DC())
    b3.place(x=190, y=400, width=350, height=100)
    
    b4 = tk.Button(root, borderwidth=1, text='Dua Lipa',  font='Arial 12', command=lambda:DL())
    b4.place(x=190, y=500, width=350, height=100)
    
    b5 = tk.Button(root, borderwidth=1, text='Billie Eilish',  font='Arial 12', command=lambda:BE())
    b5.place(x=190, y=600, width=350, height=100)
    
    b6 = tk.Button(root, borderwidth=1, text='Rihanna',  font='Arial 12', command=lambda:RI())
    b6.place(x=190, y=700, width=350, height=100)
    
    b7 = tk.Button(root, borderwidth=1, text='Fifth Harmony',  font='Arial 12', command=lambda:FH())
    b7.place(x=190, y=800, width=350, height=100)
    
    b8 = tk.Button(root, borderwidth=1, text='One Direction',  font='Arial 12', command=lambda:OD())
    b8.place(x=190, y=900, width=350, height=100)
    
    p = tk.Button(root, borderwidth=1, text='pause',  font='Arial 12', command=lambda:pa())
    p.place(x=10, y=1050, width=350, height=100)
    
    unp = tk.Button(root, borderwidth=1, text='unpause',  font='Arial 12', command=lambda:up())
    unp.place(x=360, y=1050, width=350, height=100)
    
    root.mainloop()
