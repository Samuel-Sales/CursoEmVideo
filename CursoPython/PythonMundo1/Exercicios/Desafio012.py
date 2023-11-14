# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

precoProduto = float(input('Qual o valor do produto? '))

desconto = precoProduto * 0.05
novoPreco = precoProduto - desconto

print(f'O novo preço com 5% de desconto é: R${novoPreco:.2f}')
