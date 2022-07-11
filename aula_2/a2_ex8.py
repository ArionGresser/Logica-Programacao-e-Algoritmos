# Qual é a saída de dados (output) do seguinte algoritmo: nome = "João"
# print(f"Olá {1}") # ?
# print(f"Olá {"nome"}") # ?
# print("Olá {nome}") # ?


nome = "João"
print(f"Olá {1}")           # R: Olá 1
# print(f"Olá {"nome"}")    # R: Error (unexpected indent)
print("Olá {nome}")         # R: Olá {nome}