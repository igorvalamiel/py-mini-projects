def fat(c):
    d = int(c)
    l = list(range(0, d))
    res = 0
    for a in l[::-1]:
        res *= a

def com(a, b):
    c = float(a) - float(b)
    res = fat(a)/fat(c)*fat(b)
    return res

def bin(x, y, z):
    lista = range(0, z)
    res = 0
    for a in lista:
        for b in lista[::-1]:
            res += (x**a)*(y**b)*com(a, b)
    return res

x = float(input('Digite o valor de x: '))
y  = float(input('Digite o valor de y: '))
z = int(input('Digite o valor do expoente: '))

result = bin(x, y, z)

print(f'({x} + {y}) ** {z} = {result}')
