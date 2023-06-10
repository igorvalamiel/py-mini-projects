P = tuple(int(i) for i in input('Ponto 1: ').split())
Q = tuple(int(i) for i in input('Ponto 2: ').split())

m = (Q[1]-P[1])/(Q[0]-P[0])
q = P[1]-(P[0]*m)

def intnum():
    if q%m == 0:
        return q/m
    else:
        return f'{q}/{m}'

inum = intnum()

print()
print(f'Reduzida:\ny = {m}x + {q}')
print()
print(f'Completa:\nx - y/{m} + {inum} = 0')
