# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
import math

numero = int(input('Informe o número: '))

dobro = numero * 2
triplo = numero * 3
raizQuadrada = math.sqrt(numero)

print(f'O dobro é: {dobro}')
print(f'O triplo é: {triplo}')
print(f'A raiz quadrada é: {raizQuadrada:.2f}')