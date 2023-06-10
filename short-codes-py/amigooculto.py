from random import shuffle

s = {}
n = []
sort = []
em = []

def tr():
    print('='*30)

num = int(input('Quantas pedsoas irão participar? '))

for i in range(0, num):
    tr()
    name = input(f'Digite o {i+1}* nome: ').lower()
    email = input(f'Digite o {i+1}* email: ').lower()
    n.append(name)
    s[name] = email

shuffle(n)

for i in range(0, len(n)):
    if i == len(n) - 1:
        sort.append((n[-1], n[0]))
    else:
        sort.append((n[i], n[i+1]))

for i in s.items():
    for j in sort:
        if j[1] == i[0]:
            msg = f'Você tirou {j[0]}!'
            em.append((j[1], msg, i[1]))

print(em)
    