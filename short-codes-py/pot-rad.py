opc = str(input('Você deseja fazer uma potência ou uma raiz? [p/r]: ')).lower()

while opc not in ('p', 'potencia', 'potência', 'r', 'raiz'):
    print('O valor inserido é inváido. Por favor, tente novamente.')
    opc = str(input('Você deseja fazer uma potência ou uma raiz? [p/r]: ')).lower()

if opc in ('p', 'potencia', 'potência'):
    pnum = float(input('Digite o valor da base: '))
    pexp = float(input('Digite o valor do expoente: '))
    pres = pnum ** pexp
    print(f'{pnum}^{pexp} = {pres:.3f}')

if opc in ('r', 'raiz'):
    rnum = float(input('Digite o valor da base: '))
    rexp = float(input('Digite o valor do expoente: '))
    r = 1 / rexp
    rres = rnum ** r
    print(f'{rnum}^{r:.3f} = {rres:.3f}')
