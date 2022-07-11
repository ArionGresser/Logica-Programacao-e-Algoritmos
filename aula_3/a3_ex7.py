# Escreva um script que receba um número, se esse número estiver entre 20 e 90 mostre na tela 
# "O número está na faixa entre 20 e 90" senão mostre "O número está fora da faixa".


numero = int(input('Digite qualquer valor: '))

if numero > 20 and numero < 90:
    print('O número está na faixa entre 20 e 90.')
    
else: 
    print('O número está fora da faixa.')