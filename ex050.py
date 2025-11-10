"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas
que forem pares. Se o valor digitado for ímpar, desconsidere-o."""

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"Você digitou {cont} pares e a soma entre eles é {soma}")
