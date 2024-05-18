altura = str(input('informe sua altura: ')).replace(',','.')
peso = str(input('informe seu peso: ')).replace(',','.')
altura = float(altura)
peso = float(peso)
imc = peso/(altura*altura)
print(f'{imc:,.2f}')
if imc < 18:
    print(f'abaixo do peso')
elif imc >= 18 and imc <= 24:
    print(f'normal')
elif imc >= 25 and imc <= 29:
    print(f'sobrepeso')
elif imc >= 30 and imc <= 34:
    print(f'obesidade')
elif imc >= 35 and imc <= 40:
    print(f'obesidade grau 2')
else: 
    print(f'obesidade morbida')
