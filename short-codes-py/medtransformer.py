num = float(input("Número: "))
m1 = input("Medida do número: ").lower()
m2 = input('Para qual transformar: ').lower()
#================================
def mm(x, y, z):
    la = ['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm']
    lb = ['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm']
    
    for a in range(0, 7):
        if y == la[a]:
            for b in range(0, 7):
                if z == lb[b]:
                    xx = b - a
    
    res = x * (10**int(xx))
    return res
#================================
def mm2(x, y, z):
    la = ['km2', 'hm2', 'dam2', 'm2', 'dm2', 'cm2', 'mm2']
    lb = ['km2', 'hm2', 'dam2', 'm2', 'dm2', 'cm2', 'mm2']
    
    for a in range(0, 7):
        if y == la[a]:
            for b in range(0, 7):
                if z == lb[b]:
                    xx = b - a
    
    res = x * (100**int(xx))
    return res
#================================
def mm3(x, y, z):
    la = ['km3', 'hm3', 'dam3', 'm3', 'dm3', 'cm3', 'mm3']
    lb = ['km3', 'hm3', 'dam3', 'm3', 'dm3', 'cm3', 'mm3']
    
    for a in range(0, 7):
        if y == la[a]:
            for b in range(0, 7):
                if z == lb[b]:
                    xx = b - a
    
    res = x * (1000**int(xx))
    return res
#================================
def g(x, y, z):
    la = ['kg', 'hg', 'dag', 'g', 'dg', 'cg', 'mg']
    lb = ['kg', 'hg', 'dag', 'g', 'dg', 'cg', 'mg']
    
    for a in range(0, 7):
        if y == la[a]:
            for b in range(0, 7):
                if z == lb[b]:
                    xx = b - a
    
    res = x * (10**int(xx))
    return res
#================================
def l(x, y, z):
    la = ['kl', 'hl', 'dal', 'l', 'dl', 'cl', 'ml']
    lb = ['kl', 'hl', 'dal', 'l', 'dl', 'cl', 'ml']
   
    for a in range(0, 7):
        if y == la[a]:
            for b in range(0, 7):
                if z == lb[b]:
                    xx = b - a
    
    res = x * (10**int(xx))
    return res
#================================
def pounds(x, y, z):
    if y == 'lb':
        r = x * 0.454
        res = g(r, 'kg', z)
        return res
    if z == 'lb':
        r = g(x, y, 'kg')
        res = r / 0.454
        return res
#================================
if m1[-1] == 'm':
    metro = mm(num, m1, m2)
    print(f'{num}{m1} = {metro}{m2}')

if m1[-1] == '2':
    metro2 = mm2(num, m1, m2)
    print(f'{num}{m1} = {metro2}{m2}')

if m1[-1] == '3':
    metro3 = mm3(num, m1, m2)
    print(f'{num}{m1} = {metro3}{m2}')

if m1[-1] == 'g':
    grama = g(num, m1, m2)
    print(f'{num}{m1} = {grama}{m2}')
    
if m1[-1] == 'l':
    litro = l(num, m1, m2)
    print(f'{num}{m1} = {litro}{m2}')

if m1[-2::] == 'lb':
    libras = pounds(num, m1, m2)
    print(f'{num}{m1} = {libras}{m2}')
