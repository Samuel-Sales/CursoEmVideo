# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 1.00 = R$ 3.27

dinheiroBase = float(input('Quanto de dinheiro você tem? '))

calculo = dinheiroBase / 3.27

print(f'Você pode comprar: {calculo:.2f} dolares')