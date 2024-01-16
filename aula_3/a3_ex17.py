# Desenvolva um programa que receba do usuário a sua idade e informe a situação de voto dele 
# ("Não pode votar", "Voto opcional", "Voto obrigatório"). 
# 
# Voto Opcional: maiores de 16 anos e menores de 18 anos;
# maiores de 70 anos;
#  Voto obrigatório:
# maior que 18 e menor que 70 ;
# Não pode votar:
# menor de 16 anos;


# Desenvolva um programa que receba do usuário a sua idade e informe a situação de voto dele 
# ("Não pode votar", "Voto opcional", "Voto obrigatório"). 
# 
# Voto Opcional: maiores de 16 anos e menores de 18 anos;
# maiores de 70 anos;
#  Voto obrigatório:
# maior que 18 e menor que 70 ;
# Não pode votar:
# menor de 16 anos;

print("Welcome to the national voting system, let's check if you are able to vote!")

age = int(input("Insert your age: "))

if age < 16:
    print("You can't vote. :(") 
elif age <= 17:
    print("If you want, you can vote! :)")
elif age <= 70:
    print("You must vote!")
else:
    print("If you want, you can vote! :)")