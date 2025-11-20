"""Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre
 0 e 10. Só que agora o jogador vai tentar adivinha até acertar, mostrando no final
 quantos palpites foram necessários para vencer."""

from random import randint
contador = 0

print("Sou seu computador...\n"
      "Acabei de pensar em um número entre 0 e 10.\n"
      "Será que você consegue adivinhar qual foi?")

computador = randint(0, 10)
jogador = int(input("Qual é o seu palpite? "))

while jogador != computador:
      if jogador > computador:
            jogador = int(input("Menos... Tente mais uma vez: "))
      elif jogador < computador:
            jogador = int(input("Mais ... Tente mais uma vez: "))

      contador += 1

print(f"Acertou com {contador} tentativas. Parabéns!")
