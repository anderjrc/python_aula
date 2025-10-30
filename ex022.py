"""Crie um programa que leia o nome completo de uma pessoa e mostre:
. O nome com todas as letras maiúsculoas e minúsculas.
. Quantas letras ao todo (sem considerar espaços).
. Quantas letras tem o primeiro nome."""

nome = str(input('Digite seu nome completo: '))
print(f'Seu nome em maiúscula é {nome.upper()}')
print(f'Seu nome em minúscula é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome.strip()) - nome.count(" ")} letas')
print(f"Seu primeiro nome é {nome.split()[0]} e ele tem {nome.find(' ')} letras")