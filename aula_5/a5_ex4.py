# 4) Ler um vetor de 5 elementos. Crie um segundo vetor, com todos os elementos na ordem 
# inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo 
# e assim por diante. Mostre os dois vetores. 


normal_list  = [1, 2, 3, 4, 5]

idx = len(normal_list) - 1
reverse_list = []

while (idx >= 0):
    reverse_list.append(normal_list[idx])
    idx =idx -1

print(reverse_list)
