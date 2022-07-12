# 10) Faça um programa que leia 10 números e preencha um vetor, calcule e
# mostre a quantidade de numeros negativos e a soma dos números positivos desse vetor.


numeros   = []
negativos = []
positivos = []

for i in range(10):
    valores = int(input(f"Digite um número: "))
    numeros.append(valores)
    if valores >= 0:
        positivos.append(numeros)
    else:
        negativos.append(numeros)




calc_pos = sum(positivos)
quan_neg = len(negativos)

print(f"""

Os números forneçidos foram: {numeros}
A quantidade de negativos foram: {quan_neg}
A soma dos positivos é: {calc_pos} 

""")
    