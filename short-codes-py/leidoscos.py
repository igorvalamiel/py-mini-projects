import math
print('''LEI DOS COSSENOS

Considere:
    ABC ~> Lados
    abc ~> Ângulos
    cos ~> Cosseno do ângulo
    ''')
    
elem = ['A', 'B', 'C', 'a', 'b', 'c', 'cos']
value = []

cos = 0
x = 0

print('Deixe vazio o que você deseja descobrir.')
print()
  
for i in elem:
    if i != 'cos':
        v = input(f'Valor de {i}: ').strip()
    else:
        v = input(f'Valor de {i}({x}): ').strip()
    if v == '':
        value.append(' ')
        x = i
    else:
        value.append(float(v))
    
print(elem)
print(value)