# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

valorEmMetros = float(input('Informe o valor em metros: '))

metrosParaCentimetros = valorEmMetros * 100
metrosParaMilimetros = valorEmMetros * 1000

print(f'Centimetros: {metrosParaCentimetros}')
print(f'Milimetros: {metrosParaMilimetros}')