"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
unidade: 4  dezena: 3  centena: 8  milhar: 1"""

num = int(input('Informe um número: '))
print(f'Analisando o numero {num} ...')

unidade = num % 10
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = (num // 1000) % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')

#outro jeito de fazer

num = int(input('Informe um número: '))
n = str(num)
print(f"Unidade: {(n[3])}")
print(f'Dezena: {(n[2])}')
print(f'Centena: {(n[1])}')
print(f'Milhar: {(n[0])}')
