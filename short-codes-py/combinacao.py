def fat(n):
    l = list(range(1, n+1))
    res = 1
    for a in l[::-1]:
        res *= a
    return res

def comb(x, y):
    fx = fat(x)
    fy = fat(y)
    sub = x - y
    fs = fat(sub)
    res = fx/(fy*fs)
    return res
    
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

result = int(comb(n1, n2))
print(f'C {n1}, {n2} = {result}')
