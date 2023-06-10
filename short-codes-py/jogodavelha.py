from random import choice

print('# JOGO DA VELHA #')
print()
print(' 1 | 2 | 3')
print('-----------')
print(' 4 | 5 | 6')
print('-----------')
print(' 7 | 8 | 9')
print()

#--------------------------------
def pick(x):
    while True:
        y = choice(x)
        if type(y) == str:
            pass
        else:
            break
    return int(y)

def form():
    global table
    t = table[:]
    for j, i in enumerate(t):
        if type(i) == int:
            t[j] = ' '
    
    print()
    print(f' {t[0]} | {t[1]} | {t[2]}')
    print('-----------')
    print(f' {t[3]} | {t[4]} | {t[5]}')
    print('-----------')
    print(f' {t[6]} | {t[7]} | {t[8]}')
    print()

def win():
    global table, player, bot, checklist
    t = table[:]
    p = 0
    
    if [t[0],t[1],t[2]].count(player) == 3:
        p = 'p'
    if [t[0],t[1],t[2]].count(bot) == 3:
        p = 'b'
    if [t[3],t[4],t[5]].count(player) == 3:
        p = 'p'
    if [t[3],t[4],t[5]].count(bot) == 3:
        p = 'b'     
    if [t[6],t[7],t[8]].count(player) == 3:
        p = 'p'
    if [t[6],t[7],t[8]].count(bot) == 3:
        p = 'b'
        
    print(t)
    print(p)
    if p=='p':
        print('Good Game!')
        checklist = True
    if p=='b':
        print('Loser!')
        checklist = True

def match():
    global table
    t = table[:]
    
    #horizontal (012, 345, 678)
    if t[0] == t[1]:
        return 2
    elif t[1] == t[2]:
        return 0
    elif t[0] == t[2]:
        return 1
    elif t[3] == t[4]:
        return 5
    elif t[4] == t[5]:
        return 3
    elif t[3] == t[5]:
        return 4
    elif t[6] == t[7]:
        return 8
    elif t[7] == t[8]:
        return 6
    elif t[6] == t[8]:
        return 7
    else:
        #vertical (036, 147, 258)
        if t[0] == t[3]:
            return 6
        elif t[3] == t[6]:
            return 0
        elif t[0] == t[6]:
            return 3
        elif t[1] == t[4]:
            return 7
        elif t[4] == t[7]:
            return 1
        elif t[1] == t[7]:
            return 4
        elif t[2] == t[5]:
            return 8
        elif t[5] == t[8]:
            return 2
        elif t[2] == t[8]:
            return 5
        else:
            #diagonal
            if 1 == 1:
                ok = 123
            else:
                return pick(t)
            
#--------------------------------

player = str(input('Escolha X ou O: ').upper().strip())
bot = 0

if player == 'X':
    bot = 'O'
if player == 'O':
    bot = 'X'

start = choice(('Jogador', 'Robô'))

print(f'\n{start} começa!')

table = [1,2,3,4,5,6,7,8,9]

vez = start

if start == 'Jogador':
    ppos = int(input('Qual posição? '))
    table[ppos-1] = player
    vez = 'Robô'
    print(table)
    form()
elif start == 'Robô':
    pos = choice(table)
    table[pos-1] = bot
    vez = 'Jogador'
    print(table)
    form()
    
checklist = False
    
while True:
    if vez == 'Robô':
        if start == 'Jogador':
            pos = pick(table)
            table[pos-1] = bot
            vez = 'Jogador'
        elif start == 'Robô':
            pos = pick(table)
            table[pos-1] = bot
            vez = 'Jogador'
        else:
            bpos = match()
            table[bpos] = bot
            vez = 'Jogador'
        form()
        win()
        if checklist:
            break
    if vez == 'Jogador':
        ppos = int(input('Qual posição? '))
        if type(table[ppos-1])==str:
            print('Esse espaço ja foi preenchido.')
            ppos = int(input('Qual posição? '))
        else:
            table[ppos-1] = player
        vez = 'Robô'
        form()
        win()