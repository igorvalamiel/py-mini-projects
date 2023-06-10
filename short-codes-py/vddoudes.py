from random import choice

def linha():
    print('='*40)

num = int(input('Quantas pessoas? '))

l = []

for i in range(0, num):
    l.append(input('Nome: '))
print()
while True:
    while True:
        p = choice(l)
        r = choice(l)
        if p != r:
            break

    print('Pergunta = ' + p)
    print('Responde = ' + r)
    print()
    rep = input('Mais um sorteio? ').lower()
    print()
    if rep in ['n', 'nao', 'não']:
        break
