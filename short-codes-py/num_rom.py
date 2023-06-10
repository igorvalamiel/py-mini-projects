num = str(input('Digite o número: '))

def decomp(n):
    ln = []
    alg = len(n)
    for i in range(alg):
        newn = ''
        for j in range(alg):
            if j != i:
                newn += '0'
            else:
                newn += n[j]
        ln.append(int(newn))
    return ln

def rom(x):
    n1 = 'I'
    n5 = 'V'
    n10 = 'X'
    n50 = 'L'
    n100 = 'C'
    n500 = 'D'
    n1000 = 'M'
    algs = len(x)
    lalgs = list(range(algs))
    nr = ''
    for i in x:
        for j in lalgs[::-1]:
            divid = 10**j
            divis = i/divid
            rom1, rom2 = 0
            if j == 3:
                rom1 = n1000
            if j == 2:
                rom1 = n500
                rom2 = n100
            if j == 1:
                rom1 = n50
                rom2 = n10
            if j == 0:
                rom1 = n5
                rom2 = n1
            if divis <= 3:
                for k in range(divis):
                    nr += rom1
            if divis == 4:
                nr += rom2 + rom1
    return nr

dec = decomp(num)
print(dec)
numrom = rom(dec)
print(numrom)