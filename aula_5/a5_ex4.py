# 4) Ler um vetor de 5 elementos. Crie um segundo vetor, com todos os elementos na ordem 
# inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo 
# e assim por diante. Mostre os dois vetores. 


lista_normal  = [1, 2, 3, 4, 5]

idx = len(lista_normal) - 1
lista_inversa = []

while (idx >= 0):
    lista_inversa.append(lista_normal[idx])
    idx =idx -1

print(lista_inversa)
