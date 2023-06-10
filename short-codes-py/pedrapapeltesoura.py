from random import choice

print('='*20)
print('Pedra-Papel-Tesoura')
print('='*20)
opc = str(input('Digite "start" para começar: ')).lower()


if opc == 'start':
    list = ['pedra', 'papel', 'tesoura']
    
    r = 0
    p = 0
    
    for a in range(0, 3):
        print('='*20)
        b = choice(list)
        c = str(input('Sua opção: ')).lower()
        if b == c:
            print(f'O robô escolheu: {b}')
            pass
        if b == 'pedra' and c == 'papel':
            print(f'O robô escolheu: {b}')
            p += 1
        if b == 'pedra' and c == 'tesoura':
            print(f'O robô escolheu: {b}')
            r += 1
        if b == 'papel' and c == 'pedra':
            print(f'O robô escolheu: {b}')
            r += 1
        if b == 'papel' and c == 'tesoura':
            p += 1
            print(f'O robô escolheu: {b}')
            p += 1
        if b == 'tesoura' and c == 'papel':
            print(f'O robô escolheu: {b}')
            r += 1
        if b == 'tesoura' and c == 'pedra':
            print(f'O robô escolheu: {b}')
            p += 1
    
    if p == r:
        print('='*20)
        print('O jogo ficou empatado!')
    if p > r:
        print('='*20)
        print('Você ganhou!')
    if p < r:
        print('='*20)
        print('Você perdeu!')

else:
    while opc not in ('start'):
        print("Valor inserido inválido. Por favor, tente novamente.")
        opc = str(input('Digite "start" para começar: ')).lower()
