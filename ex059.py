


n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
print("     [ 1 ] SOMAR\n"
      "     [ 2 ] MULTIPLICAR\n"
      "     [ 3 ] MAIOR NUMERO\n"
      "     [ 4 ] NOVOS NÚMEROS\n"
      "     [ 5 ] SAIR DO PROGRAMA")
opcao = int(input(">>>>>> Qual é a sua opção? "))

while opcao != 5:
    if opcao == 1:
        print(f"A soma entre {n1} + {n2} é {n1 + n2}")
    elif opcao == 2:
        print(f"O resultado de {n1} x {n2} é {n1 * n2}")
    elif opcao == 3:
        print(f"Entre {n1} e {n2} o maior valor é {max(n1, n2)}")
    elif opcao == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    else:
        print("Opção Inválida!")

    print("=-=" * 10)

    opcao = int(input(">>>>>> Qual é a sua opção? "))


print("Programa encerrado!")
