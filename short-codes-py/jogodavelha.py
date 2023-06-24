from random import choice
from time import sleep

def line():
    print('=================================================')

def check_win():
    global game_list, player, bot
    gl = game_list[:]
    winner = 0
    num_list = list(range(0, 9))

    #horizontal
    for i in num_list[::3]:
        if gl[i] == gl[i+1] == gl[i+2]:
            winner = gl[i]
    
    #vertical
    for j in num_list[:3]:
        if gl[j] == gl[j+3] == gl[j+6]:
            winner = gl[j]
    
    #diagonal
    if gl[0] == gl[4] == gl[8] or gl[2] == gl[4] == gl[6]:
        winner = gl[4]

    #retorno
    if winner == player:
        return [True, 'Player']
    elif winner == bot:
        return [True, 'Robô']
    else:
        return [False, 0]

def pick():
    global game_list
    gl = game_list[:]
    pos = 0
    while True:
        pos = choice(range(9))
        if type(gl[pos]) == int:
            break
    return pos

def player_time():
    global game_list
    pos = 0
    while True:
        pos = int(input('Escolha uma posição: ')) - 1
        if type(game_list[pos]) == str:
            print('Essa posição já está ocupada, tente novamente.')
        else:
            break
    return pos

def count_str(self):
    num = 0
    for i, k in enumerate(self):
        pos_list = []
        if type(k) == str:
            num += 1
            if num == 2:
                pos_list.append(i)
    try:
        return int(num), pos_list[0], pos_list[1]
    except:
        return int(num), 0, 1

def find_int(self):
    for i in self:
        if type(i) == int:
            return int(i-1)

def bot_time():
    global game_list
    wins = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    for l in range(8):
        for m in range(3):
            pos = wins[l][m] - 1
            wins[l][m] = game_list[pos]
    
    int_pos = 0
    for n in wins:
        num, p1, p2 = count_str(n)
        if num > 1:
            if p1 == p2:
                int_pos = int(find_int(n))
                break
            else:
                int_pos = pick()
        else:
            int_pos = pick()
    return int_pos

#=======================================================================================================
line()
print('# JOGO DA VELHA #')
print()
print(' 1 | 2 | 3')
print('-----------')
print(' 4 | 5 | 6')
print('-----------')
print(' 7 | 8 | 9')
line()
#=======================================================================================================

player = 0
while player not in ['X', 'O']:
    player = str(input('Escolha um símbolo [X ou O]: ').upper().strip())
    if player not in ['X', 'O']:
        print('Valor inserido inválido.')

if player == 'X':
    bot = 'O'
else:
    bot = 'X'

print('Escolhendo o primeiro a jogar...')
for i in range(3):
    sleep(0.9)
    print('.')

init = choice(('Player', 'Robô'))
print(f'{init} começa!')


game_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
vez = ''

if init == 'Robô':
    pos = choice((range(9)))
    game_list[pos-1] = bot
    vez = player
else:
    pos = int(input('Escolha a posição: '))
    game_list[pos-1] = player
    vez = bot

line()
win = [False, 0]
bot_count = 1
player_count = 1
while not win[0]:
    print(game_list)
    if vez == bot:
        line()
        pos = 0
        if bot_count == player_count == 1:
            pos = int(pick())
        else:
            pos = int(bot_time())
        game_list[pos] = bot
        vez = player
        bot_count += 1
    elif vez == player:
        line()
        pos = player_time()
        game_list[pos] = player
        vez = bot
        player_count += 1
    win = check_win()

if win[1] == 'Player':
    print('Parabéns, você venceu!')
else:
    print('Você perdeu para um código... melhore.')
