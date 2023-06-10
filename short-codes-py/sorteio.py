from random import choice

a = []

while True:
        c = str(input('Digite um item: '))
        a.append(c)
        d = str(input('Que adicionar mais algum item? ')).lower()
        if d in ('sim', 's'):
            pass
        elif d in ('não', 'n', 'nao'):
            break
        else:
            print('Ocorreu um erro, por favor tente novamente.')
            d = str(input('Que adicionar mais algum elemento? '))

sorteio = choice(a)

print(f'O item escolhido foi *{sorteio}*.')
