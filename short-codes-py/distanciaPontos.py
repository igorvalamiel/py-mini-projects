Xa, Ya = [float(i) for i in input('Digite o ponto A: ').split()]

Xb, Yb = [float(i) for i in input('Digite o ponto B: ').split()]

Dx = (Xa - Xb)**2
Dy = (Ya - Yb)**2

d = (Dx + Dy)**0.5

print(d)