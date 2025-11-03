"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado."""

valor_casa = float(input('Qual o valor da casa que deseja comprar: R$ '))
salario = float(input('Informe seu salário: R$ '))
anos_pagamento = int(input('Informe em quantos anos deseja pagar: '))

prestacao = valor_casa / (anos_pagamento * 12) #calculo valor da parcela
minimo = salario * 0.30 #calculando o mínimo de 30% do salário

if prestacao <= minimo:
    print(f"Para pagar uma casa de R$ {valor_casa:.2f} em {anos_pagamento} a prestação será de {prestacao:.2f}\n"
    f"Empréstimo CONCEDIDO!")
else:
    print(f"Para pagar uma casa de R$ {valor_casa:.2f} em {anos_pagamento} a prestação será de R$ {prestacao:.2f}\n"
    f"Empréstimo NEGADO!")




