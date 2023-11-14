# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2.

largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))

area = altura * largura
areaDaTinta = area / 2

print(f'Para pintar uma parede de {area:.2f}m², você precisará de {areaDaTinta:.2f} litros de tinta.')