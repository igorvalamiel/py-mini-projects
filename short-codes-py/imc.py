peso = float(input('Digite seu peso (em kg): '))

altura = float(input('Digite sua altura (em m): '))

imc = peso/(altura**2)

print(f"Seu IMC é {imc:.2f}")

if imc <= 12:
    print('Você está abaixo do peso')
    
if 12 < imc and imc <= 22:
    print('Você está no peso normal')

if 22 < imc and imc <= 32:
    print('Você está acima do peso')
    
if imc > 32:
    print('Você está com obesidade')
