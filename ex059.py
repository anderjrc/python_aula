"""Crie um programa que lea dois valores e mostre um menu como o ao lado na tela:
Seu programa deverá realizar a operação solicitada em cada caso."""
from time import sleep

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
print("     [ 1 ] SOMAR\n"
      "     [ 2 ] MULTIPLICAR\n"
      "     [ 3 ] MAIOR NUMERO\n"
      "     [ 4 ] NOVOS NÚMEROS\n"
      "     [ 5 ] SAIR DO PROGRAMA")
opcao = 0

while opcao != 5:
    opcao = int(input(">>>>>> Qual é a sua opção? "))
    if opcao == 1:
        print(f"A soma entre {n1} + {n2} é {n1 + n2}")
    elif opcao == 2:
        print(f"O resultado de {n1} x {n2} é {n1 * n2}")
    elif opcao == 3:
        print(f"Entre {n1} e {n2} o maior valor é {max(n1, n2)}")
    elif opcao == 4:
        print("Informe os números novamente:")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
        sleep(2)
    else:
        print("Opção Inválida!")
    print("=-=" * 10)

print("Programa encerrado!")
