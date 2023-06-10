import string as st

letras = list(st.ascii_lowercase)
num = []
for n in range(0, 10):
    num.append(str(n))
lista = letras + num
morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..","-----",".----","..---","...--","....-",".....","-....","--...","---..","----."]

print('[1] - Letra para morse')
print('[2] - Morse para letra')

opt = int(input())
print()

res = ''

if opt == 1:
    word = list(str(input('Digite a palavra: ')))
    for a in word:
        pos = 0
        for p, s in enumerate(lista):
            if s == a:
                pos = p
        res += f'{morse[pos]} '
    print(f'\n{res}')
elif opt == 2:
    cod = str(input('Digite o código: [use . e -][separe por espaços] '))
    m = cod.split()
    for b in m:
        pos2 = 0
        for p2, s2 in enumerate(morse):
            if s2 == b:
                pos2 = p2
        res += lista[pos2]
    print(f'\n{res}')
else:
    print('Comando inválido')
