"""Faça um algoritmo que leia o  preço de um produto e mostre seu novo preço, com 5% de desconto."""
produto = float(input('Qual é o preço do produto? R$ '))
print(f'O produto que custava R$ {produto:.3f}, na promoção com desconto de 5% vai custar R$ {produto - (produto * 5 / 100):.3f}')