"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores."""
from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0

for pessoas in range(1, 8):
    ano_nascimento = int(input("Digite um ano: "))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print(f"Ao todo tivemos {maiores} pessoas maiores de idade.\n"
      f"E também tivemos {menores} pessoas menores de idade.")
