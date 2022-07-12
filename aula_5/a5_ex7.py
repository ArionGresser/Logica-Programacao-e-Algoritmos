# 7) Ler um conjunto de numeros, armazenando-os em vetor e calcular o quadrado dos
# componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos tem 5
# elementos cada. Imprimir todos os conjuntos.

conjunto_1 = []
for i in range(5):
    numero = int(input("Digite um valor: "))
    conjunto_1.append(numero ** 2)

print(conjunto_1)

