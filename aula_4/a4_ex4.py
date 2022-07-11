# Faça um script utilizando o for, que permita ao usuário fazer três contas de subtração.
#  Para isso peça ao usuário dois números a cada iteração do loop e mostre na tela o
#  resultado da operação.

# Entrada:
# 1
# 2
# 4
# 3
# 9
# 5

# Saída:
# 1 - 2 = -1
# 4 - 3 = 1
# 9 - 5 = 4



for i in range(3):
   number1 = int(input("Type the first number: "))
   number2 = int(input("Type the second number: "))

   result = number1 - number2
   print(f"{number1} - {number2} = {result}")

print("Programa finalizado...")
