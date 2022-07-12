# 5) Ler um vetor com 5 nomes de pessoas, após pedir que o usuário digite um nome qualquer 
# de pessoa. Escrever a mensagem “ACHEI”, se o nome estiver armazenado no vetor de nomes ou 
# “NÃO ACHEI” caso contrário. 


nomes = ["Arion", "Lorenzo", "Luciano", "William", "Bruna" ]

nome = str(input("Digite seu nome da lista de convidados: "))

if nome in nomes:
    print("ACHEI!")

else:
    print("NÃO ACHEI!")

