# Leia um número. Se o número for positivo imprima a raiz quadrada desse número. 
# Do contrário, imprima o número ao quadrado.

import math


number = int(input("Insira um número: "))

if number > 0:
    print("A raiz quadrada é:", end=" ")
    print(math.sqrt(number))

else:
    print("O quadrado do número é:", end=" ")
    print(number ** 2)