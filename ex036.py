"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado."""

valor_casa = float(input('Qual o valor da casa que deseja comprar: R$ '))
salario = float(input('Informe seu salário: R$ '))
anos_pagamento = int(input('Informe em quantos anos deseja pagar: '))

valor_parcela = valor_casa / (anos_pagamento * 12) #calculo valor da parcela
limite_credito = salario - (salario * 0.30)
