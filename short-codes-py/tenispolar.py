print(" TENIS POLAR ")
print()
print('Não utilize acentos gráficos!')
print()

txt = str(input('Digite o texto para que ele possa ser codificado ou decodificado: ')).lower()
newtxt = ''

for i in txt:
    if i == 't':
        newtxt += 'p'
    elif i == 'e':
        newtxt += 'o'
    elif i == 'n':
        newtxt += 'l'
    elif i == 'i':
        newtxt += 'a'
    elif i == 's':
        newtxt += 'r'
    elif i == 'p':
        newtxt += 't'
    elif i == 'o':
        newtxt += 'e'
    elif i == 'l':
        newtxt += 'n'
    elif i == 'a':
        newtxt += 'i'
    elif i == 'r':
        newtxt += 's'
    else:
        newtxt += i

print()
print(newtxt)