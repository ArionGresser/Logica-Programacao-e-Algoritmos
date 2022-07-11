# Escreva um script que receba três valores A, B, C. Faça as comparações necessárias para exibir na tela o maior valor entre os três.

v_1 = int(input('Digite o primeiro valor: '))
v_2 = int(input('Digite o segundo valor: '))
v_3 = int(input('Digite o terceiro valor: '))

maior_numero = max(v_1, v_2, v_3)
print('o maior valor é:', maior_numero)