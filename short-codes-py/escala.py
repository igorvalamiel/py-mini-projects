D = str(input("Distância Real [em m]: "))
d = str(input("Distância no mapa [em cm]: "))
E = str(input("Escala: "))

try:
    DD = float(D)
except:
    pass
    
try:
    dd = float(d)
except:
    pass
    
try:
    EE = float(E)
except:
    pass

print()

if D == '':
    rD = EE * dd
    print(f'A distância real é de {rD}')
if d == '':
    rd = DD / EE
    print(f'A distância no mapa é de {rd}')
if E == '':
    rE = DD / dd
    print(f'A escala é 1:{rE:.0f}00')
