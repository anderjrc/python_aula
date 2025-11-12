"""Crie um programa que leia um frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços."""

frase = str(input("Digite uma frase: ")).replace(" ","").upper()#replace é pra tirar todos os espaçamentos
palindromo = frase[::-1]
print(f"O inverso de {frase} é {palindromo}")
if frase == palindromo:
    print(f"Temos um palíndromo!")
else:
    print("Não temos um palíndromo")





