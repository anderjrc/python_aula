"""Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade
 de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia
  e R$0,15 por km rodado."""

dias_alugado = int(input('Quantos dias alugados? '))
km_rodado = float(input('Quantos km rodados? '))
print(f'O total a pagar é de R$ {(dias_alugado * 60) + (km_rodado * 0.15):.2f}')


