def temperatura():
    base = str(input('Qual é a medida de temperatura base? [C, F, K] ')).upper()
    trans = str(input('Para qual medida você quer transformar? [C, F, K] ')).upper()
    return base, trans

x, y = temperatura()

a = float(input(f"Digite a temperatura em {x}: "))

z = 0

if x == y:
    print('Ambas as temperaturas estão na mesma medida.')
else:
    if x == 'C':
        if y == 'F':
            z = (a*1.8)+32
        if y == 'K':
            z = a+273
    if x == 'F':
        if y == 'C':
            z = (a-32)/1.8
        if y == 'K':
            z = ((a-32)*(5/9))+273
    if x == 'K':
        if y == 'C':
            z = a-273
        if y == 'F':
            z = ((a-273)*1.8)+32

print(f"{a}{x} é igual ou aproximadamente a {z}{y}")
