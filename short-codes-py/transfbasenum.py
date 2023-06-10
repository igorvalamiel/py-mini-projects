num = int(input('Digite um número inteiro: '))
b1 = int(input('Qual a base desse número? '))
b2 = int(input('Para qual base quer transformar? '))
num2 = ''
num0 = num

if b1 == 0 or b2 == 0:
    print('Não foi possível calcular pois não existe base numérica 0.')
if b1 == 1 or b2 == 1:
    print('Não foi possível calcular pois não existe base numérica 1.')

def base10():
        global num, b1, b2, num2, num0
        res = 0
        res2 = ''
        r = ''
        n = str(num)
        lista = list(range(0, len(str(num))))

        for a in lista[::-1]:
            res2 += n[a]
        for b, c in enumerate(res2):
            res += int(c)*(b1**b)

        if b2 == 10:
            num2 = str(res)
        else:
            num = res
            b1 == 10
            r = 1
        res = ''
        result = ''
        while r != 0:
            r = num // b2
            res += str(num - (b2*r))
            num = r
        for a in res[::-1]:
            result += a
        num2 = result

if b2 <= 10:
    if b1 != 10:
    #transformando para a base 10
        base10()
    #transformando da base 10 para outra
    if b1 == 10:
        r = 1
        res = ''
        result = ''
        while r != 0:
            r = num // b2
            res += str(num - (b2*r))
            num = r
        for a in res[::-1]:
            result += a
        num2 = result
    
    print(f'\n{num0} (base {b1}) em base {b2} é {num2}')

if b2 > 10:
    print('Ainda não é possível calcular...')
