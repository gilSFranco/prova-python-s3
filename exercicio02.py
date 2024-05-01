import os

os.system('cls')

comprimento = float(input('Qual é o comprimento desse terreno? '))
largura = float(input('E a largura dele? '))

area = comprimento * largura

print(f'A área do terreno equivale á: {area:.2f}m²')