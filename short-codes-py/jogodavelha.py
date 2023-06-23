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
while not win[0]:
    print(game_list)
    if vez == bot:
        line()
        print('Vez do robo')
        vez = player
    elif vez == player:
        line()
        pos = player_time()
        game_list[pos] = player
        vez = bot
    win = check_win()

if win[1] == 'Player':
    print('Parabéns, você venceu!')
else:
    print('Você perdeu para um código... melhore.')
