# Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se
# encontram o maior e o menor valor.

valor = int(input("Digite 1° valor : "))
valor_maior = valor
valor_menor = valor


for i in range(4):
    valor = int(input(f"Agora o {i + 2}° valor: "))
    if valor > valor_maior:
        valor_maior = valor
    elif valor < valor_menor:
        valor_menor = valor

print("Maior valor:", valor_maior) 
print("Menor valor:", valor_menor)
