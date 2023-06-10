def juros(x, y):
    ad = x * (y / 100)
    return ad

y = float(input("Digite o valor inicial: "))
x = float(input("Digite o valor da porcentagem mensal: "))
z = int(input("Digite quantos meses serão rendidos: "))

for a in range(1, z+1):
    ad = juros(x, y)
    y += ad
    

print(f"O valor total após {z} meses, com juros de {x}%, será {y:.2f}.")
