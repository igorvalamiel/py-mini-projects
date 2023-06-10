xx = str(input('Digite o genótipo da mãe: '))
xy = str(input('Digite o genótipo do pai: '))

rec = str(xx[0].lower() + xx[0].lower())

t1 = xx[0]+xy[0]
t2 = xx[0]+xy[1]
t3 = xx[1]+xy[0]
t4 = xx[1]+xy[1]

l = [t1, t2, t3, t4]

d = 0
r = 0

for g in l:
    if g == rec:
        r += 1
    else:
        d += 1

pd = (d/4)*100
pr = (r/4)*100

print()

print(f'A probabilidade do filho ser DOMINANTE é {pd:.1f}%, e a do filho ser RECESSIVO é {pr:.1f}%.')
