from random import choice

def red(x):
    return f'\033[31m{x}\033[m'
    
def yellow(x):
    return f'\033[33m{x}\033[m'

def green(x):
    return f'\033[32m{x}\033[m'

def rcolor(x):
    a = f'\033[42m{x}\033[m'
    return f'\033[30m{a}\033[m'

def p(x):
    b = ''
    for a in x:
        b += a
    return b

def gg():
    glist = []
    guess = []
    res = []
    
    num = 0
    
    for b in range(0, 4):
        opc = choice(range(0, 10))
        if opc in glist:
            pass
        else:
            glist.append(str(opc))
    
    while True:
        print('='*30)
        num += 1
        guess = []
        res = []
        chute = input('')
        for c in chute:
            guess.append(c)
            res.append(c)
        for d in range(0, 4):
            if guess[d] not in glist:
                guess[d] = red(guess[d])
            else:
               if guess[d] == glist[d]:
                   guess[d] = green(guess[d])
               else:
                   guess[d] = yellow(guess[d])
        for e in guess:
            print(e, end='')
        print()
        if glist == res:
            print()
            print("Você acertou!")
            break
        if num == 6:
            let = p(glist)
            r = rcolor(let)
            print()
            print(f"Você perdeu! O número era " + str(r))
            break

gg()
while True:
    g = input('Quer jogar de novo? ').lower()
    if g in ('n', 'nao', 'não'):
        print("="*30)
        print('Muito obrigado por jogar!')
        break
    if g in ('s', 'sim'):
        gg()
