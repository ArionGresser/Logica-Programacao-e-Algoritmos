# 1) Crie uma função que receba uma array e retorne o primeiro e o último elemento desse array como um novo array.
# O array pode ter qualquer tamanho.



lista_1 = []

for i in range(5):
   numeros = int(input(f"Digite o {i + 1}° número: "))
   lista_1.append(numeros)

lista_2 = lista_1[0], lista_1[-1]


print(lista_2)
    