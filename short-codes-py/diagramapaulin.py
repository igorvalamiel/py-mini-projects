dp = list('1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p6'.split())
dpnum = []

ele = int(input('Quantos elétrons o átomo tem? '))
soma = 0
pos = 0
dif = 0

for i in dp:
    n = ''
    try:
        n += i[2] + i[3]
    except:
        n += i[2]
    dpnum.append(int(n))
    
for j, k in enumerate(dpnum):
    soma += k
    if soma > ele:
        pos = j
        dif = soma - ele
        break
        
res = ''
for l, m in enumerate(dp):
    if l == pos:
        value = dpnum[pos]
        new_value = value - dif
        new_ele = m[0] + m[1] + str(new_value)
        if new_value != 0:
            res += new_ele + ' '
        break
    else:
        res += m + ' '

print()
print(dp)
print(pos, dif)
print(res)