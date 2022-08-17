# Desenvolva um programa que receba do usuário a sua idade e informe a situação de voto dele 
# ("Não pode votar", "Voto opcional", "Voto obrigatório"). 
# 
# Voto Opcional: maiores de 16 anos e menores de 18 anos;
# maiores de 70 anos;
#  Voto obrigatório:
# maior que 18 e menor que 70 ;
# Não pode votar:
# menor de 16 anos;


age = int(input("Type your age: "))


if age < 16:
    print("Can't Vote.")
elif age > 70:
    print("Opitional Vote.")
elif age >= 18:
    print("Mandatory Vote.")
elif age < 18:
    print("Opitional Vote.")
elif age < 70:
    print("Mandatory Vote.")