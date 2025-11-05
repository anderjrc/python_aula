""""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

print("=" * 15, "LOJAS ANDER", "=" * 15)
compra = float(input("Preço das compras: R$ "))
print("FORMAS DE PAGAMENTO\n"
      "[ 1 ] à vista dinheiro/cheque\n"
      "[ 2 ] à vista no cartão\n"
      "[ 3 ] 2x no cartão\n"
      "[ 4 ] 3x ou mais no cartão")
opcao = int(input("Qual opção de pagamento: "))

if opcao == 1:
    total = compra - (compra * 0.10)
elif opcao == 2:
    total = compra - (compra * 0.05)
elif opcao == 3:
    total = compra
    parcela = compra / 2
    print(f"Sua compra será parcelada em 2x de R$ {parcela:.2f}")
elif opcao == 4:
    total = compra + (compra * 0.20)
    parcela = total / 3
    print(f"Sua compra será parcelada em 3x de R$ {parcela:.2f}")
else:
    total = compra
    print("Opção inválida!")

print(f"Sua compra de R$ {compra:.2f} vai custar R$ {total:.2f} no final.")



"""if opcao == 1:
    print(f"Você selecionou a opção 1 e terá 10% de desconto, sua compra ficará R$ {compra - (compra * 0.10):.2f}.")
elif opcao == 2:
    print(f"Você selecionou a opção 2 e terá 5% de desconto, sua compra ficará R$ {compra - (compra * 0.05):.2f}.")
elif opcao == 3:
    print(f"Você selecionou a opção 3 e sua compra ficará no valor normal do produto.")
elif opcao == 4:
    print(f"Você selecionou a opção 4 e 20% de juros e sua compra ficará {compra + (compra * 0.20):.2f}")"""
