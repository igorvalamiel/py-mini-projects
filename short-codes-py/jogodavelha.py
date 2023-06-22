from random import choice
from time import sleep

def line():
    print('=================================================')
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

win = False
while not win:
    line()
    print(game_list)
    if vez == bot:
        print('Vez do robo')
        break
    elif vez == player:
        print('Vez do jogador')
        break
