# Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. 
# Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

import math


numero = int(input('Forneça-me um número positivo e eu te direito a raiz: '))

if numero > 0:
    print(math.sqrt(numero))
elif numero < 0:
    print('O número é inválido..')