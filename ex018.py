"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""

import math
ang = float(input('Digite o ângulo que voçê deseja: '))
ang_radiano = math.radians(ang)
print(f'O ângulo de {ang} tem {math.sin(ang_radiano):.2f}')
print(f'O ângulo de {ang} tem {math.cos(ang_radiano):.2f}')
print(f'O ângulo de {ang} tem {math.tan(ang_radiano):.2f}')
