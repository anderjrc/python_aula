"""Faça um algoritimo que leia o salário de um funcionário e mostres seu novo salário, com 15% de aumento."""
salario = float(input('Qual é o salário do funcionário? R$ '))
print(f'Um funcionário que ganhava R$ {salario:.3f}, com 15% de aumento, passa a receber R$ {salario + (salario * 15 / 100):.3f}')
