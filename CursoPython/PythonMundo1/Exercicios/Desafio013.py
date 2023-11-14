# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento

salario = float(input('Informe o seu salario: '))

aumento = salario * 0.15

novoSalario = salario + aumento
print(f'O novo salario eh: {novoSalario:.2f}')
