from random import choice

tam = eval(input("Qual será o tamanho da tabela? (00,00) "))
table = [[0 for i in range(tam[1])] for j in range(tam[0])]
num = int(input("Quantas palavras deverão ser encontradas? "))
l = []
for i in range(num): l.append(str(input()))
print(table)
