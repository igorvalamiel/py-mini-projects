import random as ram
from time import sleep

lista = []
sorteado = []
for a in range(1, 91):
    lista.append(a)

b = 0

print("="*30)
print("BINGO")
print("="*30)

start = int(input("Digite 0 para começar: "))

if start != 0:
    while True:
        print("Valor inválido, tente novamente.")
        start = int(input("Digite 0 para começar:"))
        if start == 0:
            break

if start == 0:
    while b != 90:
        num = ram.choice(lista)
        if num not in sorteado:
            print(num)
            sorteado.append(num)
            b =+ 1
            sleep(10)
