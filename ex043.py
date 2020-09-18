peso = float(input('Qual é o seu peso: '))
altura = float(input('Wual é sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print("Sobrepeso.")
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')