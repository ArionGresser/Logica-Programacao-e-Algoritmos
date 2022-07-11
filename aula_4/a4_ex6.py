# Faça um programa que peça ao usuario para digitar 5 valores. Ao final, mostre a soma 
# desses valores e média desses valores (arredondado para duas casas decimais).
# Entrada:
# 9
# 8
# 2
# 3
# 4

# Saída:
# Soma: 26
# Média: 5.20



for i in range(1):
    value1 = float(input("Type the first note: "))
    value2 = float(input("Type the second note: "))
    value3 = float(input("Type the third note: "))
    value4 = float(input("Type the fourth note: "))
    value5 = float(input("Type the fifth note: "))

    sum = value1 + value2 + value3 + value4 + value5
    average = sum / 5

    print(f"Sum: {sum}")
    print(f"Average: {average}")


    
