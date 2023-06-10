from random import shuffle

def fat(y):
    x = 1
    for a in range(1, len(y)+1):
        x *= int(a)
    return x

def f(y):
    x = 1
    for a in range(1, y+1):
        x *= int(a)
    return x

def res(x):
    y = ''
    for a in x:
        y += a
    return y

word = list(str(input('Digite a palavra: ')))

l = []
rl =[]

n1 = fat(word)
n2 = 1

for b in word:
    x = word.count(b)
    if b not in rl:
        rl.append(b)
        n = f(x)
        n2 *= n

num = n1/n2

while True:
    shuffle(word)
    if res(word) not in l:
        l.append(res(word))
    if len(l) == num:
        break

print()
for i in l:
    print(i)
