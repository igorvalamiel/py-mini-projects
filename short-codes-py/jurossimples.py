def juros(x, y):
    z = x * (y/100)
    return z

num = float(input("Digite o valor inicial: "))
porc = float(input("Digite o valor da porcentagem mensal: "))
mes = int(input("Digite quantos meses serão rendidos: "))

tot = num

for a in range(1, mes+1):
    tot += juros(num, porc)

print(f"O valor total após {mes} meses, com juros de {porc}%, será {tot:.2f}.")