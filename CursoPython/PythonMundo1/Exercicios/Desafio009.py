# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

numero = int(input('Informe o número: '))

for i in range(1, 11) :
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')