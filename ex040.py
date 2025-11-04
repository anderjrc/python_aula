"""Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
- Média abaixo 5.0 : REPROVADO
- Média entre 5.0 e 6.9 : RECUPERAÇÃO
- Média entre 7.0 ou superior : APROVADO"""

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2

if media <= 5.0:
    print(f"Sua média foi {media}, está REPROVADO!\n"
          f"Estude mais.")
elif media > 5.0 and media <= 6.9:
    print(f"Sua média foi {media}, está de RECUPERAÇÃO!\n"
          f"Estude mais.")
elif media > 7.0 and media <= 10.0:
    print(f"Sua média foi {media}, você está APROVADO!\n"
          f"PARABÉNS")
else:
    print("Valor inválido!")