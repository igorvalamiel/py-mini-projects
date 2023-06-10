def num_rom(x):
    res = ''
    if x == 1:
        res = 'I'
    if x == 2:
        res = 'II'
    if x == 3:
        res = 'III'
    if x == 4:
        res = 'IV'
    if x == 5:
        res = 'V'
    if x == 6:
        res = 'VI'
    if x == 7:
        res = 'VII'
    if x == 8:
        res = 'VIII'
    if x == 9:
        res = 'IX'
    if x == 10:
        res = 'X'
    if x == 11:
        res = 'XI'
    if x == 12:
        res = 'XII'
    if x == 13:
        res = 'XIII'
    if x == 14:
        res = 'XIV'
    if x == 15:
        res = 'XV'
    if x == 16:
        res = 'XVI'
    if x == 17:
        res = 'XVII'
    if x == 18:
        res = 'XVIII'
    if x == 19:
        res = 'XIX'
    if x == 20:
        res = 'XX'
    if x == 21:
        res = 'XXI'
    if x == 22:
        res = 'XXII'
    if x == 23:
        res = 'XXIII'
    if x == 24:
        res = 'XXIV'
    if x == 25:
        res = 'XXV'
    if x == 26:
        res = 'XXVI'
    if x == 27:
        res = 'XXVII'
    if x == 28:
        res = 'XXVIII'
    if x == 29:
        res = 'XXIX'
    if x == 30:
        res = 'XXX'
    if x == 50:
        res = 'L'
    if x == 100:
        res = 'C'
    if x == 1000:
        res = 'M'
    return res

ano = str(input("Digite o ano: "))

alist = []

for a in ano:
    alist.append(a)
for b in range(0, 2):
    del alist[-1]

cem = alist[0] + alist[1]
sec = int(cem) + 1

s = num_rom(sec)

print(f"Esse ano pertence ao séc.{s}")
