print('Digite a ordem da matriz: ')
m, n = [int(i) for i in input().split('x')]

matriz = []
for i in range(1, m+1):
    for j in range(1, n+1):
        matriz.append(int(input(f'Digite o valor de a{i}{j}: ')))       

def mat():
    global m
    a = 0
    for x in matriz:
        print(x, end=' ')
        a+=1
        if a == m:
            print()
            a = 0

if m != n:
    print('Essa matriz não é quadrada.')
else:
    d = 0
    if m == 1:
        d = matriz[0]
    if m == 2:
        v1 = matriz[0] * matriz[3]
        v2 = matriz[1] * matriz[2]
        d = v1 - v2
    if m == 3:
        v1 = 0
        v2 = 0
        v1 += matriz[0]*matriz[4]*matriz[8]
        v1 += matriz[1]*matriz[5]*matriz[6]
        v1 += matriz[2]*matriz[3]*matriz[7]
        v2 += matriz[2]*matriz[4]*matriz[6]
        v2 += matriz[0]*matriz[5]*matriz[7]
        v2 += matriz[1]*matriz[3]*matriz[8]
        d = v1 - v2
    print(f'A determinante da matriz é {d}.')

mat()