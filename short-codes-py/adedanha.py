from random import shuffle

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

shuffle(alfabeto)

for a in alfabeto:
    x = input("Digite OK para sortearbuma letra e EXIT para sair: ").upper()
    if x == 'OK':
        print(a)
