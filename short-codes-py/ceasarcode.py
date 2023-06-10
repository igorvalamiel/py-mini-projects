import string as st

print(" CEASAR CODE ")
print()
opc = int(input('Digite 1 para codificar ou 2 para decodificar:'))
print()
print('Não utilize acentos gráficos!')
print()

al = st.ascii_lowercase
alc = ''

for x in al[3::]:
    alc += x
for y in al[:3:]:
    alc += y

ret = ''

if opc == 1:
    pal = str(input('Digite a palavra: ')).lower()
    for b, a in enumerate(pal):
        if a in al:
            pos = al.find(a)
            ret += alc[pos]
        else:
            ret += a
    print()
    print(ret)
elif opc == 2:
    cod = str(input('Digite o código: ')).lower()
    for b1, a1 in enumerate(cod):
        if a1 in al:
            pos1 = alc.find(a1)
            ret += al[pos1]
        else:
            ret += a1
    print()
    print(ret)
else:
    print('Comando inválido!')
