import string as st
from random import choice

letras = list(st.ascii_lowercase)

nl = int(input("Quantas letras a palavra deverá ter? "))

pl = ''

def palavra(x):
    global pl
    for a in range(0, x):
        ch = choice(letras)
        pl += ch
    print(pl)

while True:
    palavra(nl)
    opc = str(input("Deseja refazer o nome? ")).lower()
    if opc in ['nao', 'não', 'n', 'ñ']:
        break
    else:
        pl = ''
        pass
