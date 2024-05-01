import os

os.system('cls')

produto = float(input('Qual o valor da compra? '))

if produto > 20.0:
    percentual = 30 / 100
    compra = produto + (produto * percentual)

    print(f'O valor final da compra é de: {compra}.')
else:
    percentual = 45 / 100
    compra = produto + (produto * percentual)

    print(f'O valor final da compra é de: {compra}.')