"""Escreva um progama que leia um número n inteiro qualquer e emsotre na tela os n
primeiros elementos de uma Sequência de Fibonacci."""

print("-" * 25)
print("Sequência de Fibonacci")
print("-" * 25)
num = int(input("Quantos termos você quer mostrar? "))
termo1 = 0
termo2 = 1
print("~" * 20)
print(f"{termo1} > {termo2}", end="")
contador = 3
while contador <= num:
    termo3 = termo1 + termo2
    print(f" > {termo3}", end="")
    termo1 = termo2
    termo2 = termo3
    contador += 1
print(" > FIM")
print("~" * 20)