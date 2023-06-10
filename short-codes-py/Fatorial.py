def n(a):
    b = 1
    negative = False
    if a < 0:
        a *= -1
        negative = True
    for c in range(0, a):
        b *= a-c
    if negative:
        if not a % 2 == 0:
            b *= -1
    return b
        
        
x = int(input('Digite um número inteiro: '))
y = n(x)
print(f'{x}! = {y}')
