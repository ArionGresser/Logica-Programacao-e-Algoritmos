# 3) Faça um programa que receba do usuario um vetor com 5 posições. Em seguida, mostre
# o maior e o menor elemento do vetor.


lista_nums = []

for i in range(5):
   nums = int(input("Digite um numero: "))
   lista_nums.append(nums)

print("o maior valor da lista e: ", max(lista_nums))
print("O menor valor da lista e: ", min(lista_nums))
