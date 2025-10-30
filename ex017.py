"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo,
calcule e mostre o comprimento da hipotenusa."""

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do catetto adjacente: '))
print(f'A hipotenusa vai medir {hypot(co, ca):.2f}')
