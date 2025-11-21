"""Crie um progrma que faça o computaadorjogar Kokenpô com você."""

import random
from time import sleep
print("Suas opções:\n"
      "[ 0 ] Pedra\n"
      "[ 1 ] Papel\n"
      "[ 2 ] Tesoura")

escolha = int(input("Qual é sua jogada? "))
pc = [0, 1, 2]
random.choice(pc)
print("JO")
sleep(2)
print("KEN")
sleep(2)
print("PÔ!!!")

if escolha == 0 and pc ==