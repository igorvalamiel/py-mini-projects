import math

num = float(input('Digite um número: '))
trig = str(input('Digite o que deseja descobrir [sen, cos, tg]: ')).lower()

if trig == 'sen':
    x = math.sin(num *  math.pi / 180)
elif trig == 'cos':
    x = math.cos(num * math.pi / 180)
elif trig == 'tg':
    x = math.tan(num * math.pi / 180)
else:
    while trig not in ('sen', 'cos' 'tg'):
        print('Você digitou um número inválido, digite apenas "sen", "cos" ou "tg".')
        trig = str(input('Digite o que deseja descobrir [sen, cos, tg]: ')).lower()
    
print(f"{trig}({num}) = {x:.2f}")