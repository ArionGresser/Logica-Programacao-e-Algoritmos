# Escreva um script para ler um número e informar se ele é divisível por 5.

numero = int(input('Diga-me um número e eu direi se é divisível por 5: '))

if numero % 5 == 0:
    print("Este número é sim divisível por 5!")
elif numero % 5 != 0:
    print("Este número não é divisível por 5!")