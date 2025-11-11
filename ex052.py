"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

cont = 0

num = int(input("Digite número: "))
for i in range(1, num + 1):
    print(f"{i}", end=" ")
    if num % i == 0:
        cont += 1
print(f"\nO número {num} foi divisível {cont} vezes")

if cont == 2: # número primo não pode ser divisível mais do que 2x, geralmente ele é divisível pelo número 1 e por ele mesmo
    print("Ele É PRIMO!")
else:
    print("Ele não É PRIMO!")


"""for i in range(0):
    if num % i == 0:
        print(i)
        divisor += 1
if divisor == 2:
    print(f"Ele É PRIMO.")
else:
    print(f"Ele NÃO É PRIMO.")"""



