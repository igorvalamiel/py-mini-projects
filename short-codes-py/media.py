num = int(input("Quantos números serão informados? "))

x = 0

for a in range(0, num):
    x += float(input(f'Número {a+1}: '))

media = x / num

print()
print(f"A média desses números é {media}")
