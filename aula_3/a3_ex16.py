# Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) 
# e informe se o resultado foi um empate, a vitória do primeiro time ou do segundo time.

team_one = int(input("Type the goals of the team one: "))
team_two = int(input("Type the goals of the team two: "))
 
if team_one == team_two:
    print("The game tied!")

elif team_one > team_two:
    print("Team One is the Winner!")

elif team_one < team_two:
    print("Team Two is the Winner!")