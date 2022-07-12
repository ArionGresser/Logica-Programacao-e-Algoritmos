# 2) Escreva um programa que leia 5 numeros e os armazene em um vetor. Mostre o vetor, o 
# maior elemento e a posição que ele se encontra.



numbers  = []
maior    = 0
posicao  = 0
for i in range(5):
    valor = int(input(f"Adicione o {i + 1}° numero: "))
    numbers.append(valor)
    if i == 0:
        maior = valor
        posicao = i
    elif valor > maior:
        maior = valor
        posicao = i

print(f"O maior valor e: {maior} e esta na posicao: {posicao}")

