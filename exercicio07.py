import os

os.system('cls')

valores = input('Digite numeros espaçados por espaços: ')

numeros = [int(x) for x in valores.split()]

for i in numeros:
    print(i)