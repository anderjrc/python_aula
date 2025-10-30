"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, Calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Informe o valor do seu salário para saber o aumento: '))
if salario <= 1250:
    print(f"Com o salário de R$ {salario:.2f} seu novo salário será R$ {salario + (salario * 0.15):.2f}")
else:
    print(f"Com o salário de R$ {salario:.2f} seu novo salário será R$ {salario + (salario * 0.10):.2f}")