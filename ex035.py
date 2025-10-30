"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""

print('-=' * 15)
print('Analisador de Triângulos')
print('-=' * 15)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a > b + c and b > a + c and c > a + b:
    print("Os segmentos a cima PODEM FORMAR triângulo!")
else:
    print("Os segmentos a cima NÃO PODEM FORMAR triângulo!")
