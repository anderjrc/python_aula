"""Refaça o DESAFIO 009, mostrando a tabuada d eum número que o usuário escolher,
só que agora utilizando um laço for."""

num = int(input("Digite um número para saber sua tabuada: "))
for mult in range(1, 11): #usei o termo mult para referência de multiplicação
    print(f"{num} x {mult} = {num * mult}")

