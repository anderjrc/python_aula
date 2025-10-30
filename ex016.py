"""Crie um programa que leia um número Real qualquer pelo teclado e mostre no tela a sua porção interia.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6."""

from math import trunc
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e sua porção inteira é {trunc(num)}')
