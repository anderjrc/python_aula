"""Faça um programa que leia um número qualquer e mostre o seu fatorial."""
#Primeiro jeito de fazer
from math import factorial

num = int(input("Digite um número para caluclar seu Fatorial: "))
resultado = factorial(num)
print(f"Calculando fatorial de {num} o resultado é {resultado}")

#Segundo jeito de fazer
num = int(input("Digite um número para caluclar seu Fatorial: "))
contador = num
fatorial = 1
while contador > 0:
    print(f"{contador}", end="")
    print(" x " if contador > 1 else " = ", end="")
    fatorial *= contador
    contador -= 1
print(f"{fatorial}")