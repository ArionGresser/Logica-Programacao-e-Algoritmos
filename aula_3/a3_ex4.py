# Escreva um script que receba um número, se esse número for par mostre na tela a metade do número digitado.
# No final do script mostrar na tela "Programa finalizado..."

numero = int(input("Digite o valor desejado: "))

if numero % 2 == 0:
    print(numero / 2)
    
print('Programa Finalizado...')