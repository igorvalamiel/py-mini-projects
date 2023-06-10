import string as st

alpha = str(st.ascii_lowercase)
num = []

for a in range(1, 27):
    num.append(str(a))

def cod(x):
    txt = ''
    for a in x:
        pos = alpha.find(a)
        txt += num[pos]
        txt += ' '
    return txt
    
def decod(x):
    txt = ''
    for a in x:
        if a == ' ':
            txt += ''
        else:
            pos = num.find(a)
            txt += alpha[pos]
    return txt

v1 = str(input('Você deseja codificar[1] ou decodificar[2]? ')).lower()

res = ''

if v1 in ['codificar', '1']:
    v2 = str(input('Digite o que deseja codificar: '))
    res = cod(v2)
elif v1 in ['decodificar', '2']:
    v3 = str(input('Digite o que deseja decodificar: '))
    res = decod(v3)
else:
    print('Erro, tente novamente.')

print(res)
