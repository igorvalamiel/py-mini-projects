def equa_seg_grau(a, b, c):
    x1 = (-b + (((b**2) - (4*a*c))**0.5)) / (2*a)
    x2 = (-b - (((b**2) - (4*a*c))**0.5)) / (2*a)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")


a = float(input("Digite o coeficiente 'a': "))        
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))
print()
equa_seg_grau(a, b, c)
