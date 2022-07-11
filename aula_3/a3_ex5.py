# Escreva um script que receba um número, se esse número for ímpar mostre na tela o quadrado do número digitado.
# No final do script mostrar na tela "Programa finalizado..."


numero = int(input('Digite o valor necessário: '))

if numero % 2 != 0:
    print(numero ** 2)

print("Operação Finalizada...")