"""Crie um programa que leia o nome d euma pessoa e diga se ela tem "Silva" no nome."""

nome = str(input('Qual é o seu nome completo: ')).strip()
#print(nome[:5].upper() == 'SILVA')
print(f"Seu nome em Silva? {'silva' in nome.lower()}")


