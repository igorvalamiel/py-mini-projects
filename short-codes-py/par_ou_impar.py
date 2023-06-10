def par(x):
    if x%2 == 0:
        return True
    else:
        return False

x = int(input('Digite um número: '))
if par(x):
    print("Esse número é par.")
else:
    print("Esse número é ímpar.")