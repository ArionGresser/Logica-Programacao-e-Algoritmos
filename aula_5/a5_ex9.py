# 9) Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois
# valores X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa
# deverá escrever a soma dos valores encontrados nas respectivas posições X e Y. Se o usuário
# digitar valores inválidas para X ou Y mostre uma mensagem de erro e peça novos valores até 
# que ambos os valores sejam válidos.



from timeit import repeat


vetores = ["X", "Y"]
for i in range(8):
    vetor = int(input(f"Digite o {i + 1}∘ : "))
    vetores.append(vetor)

vetores[0] = int(input("Digite um valor para X: "))
vetores[1] = int(input("Digite um valor para Y: "))

print(vetores[0] + vetores[1])
