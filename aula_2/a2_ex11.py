# Crie um algoritmo que:

# Receba a altura e a largura de um retângulo
# Calcule a área e o perímetro do retângulo
# Mostre a área e o perímetro calculados
 


# Input
altura   = float(input("Digite a Altura: "))
largura  = float(input("Digite a largura: "))

# Process

area      = altura * largura
perimetro = (altura * 2) + (largura * 2)

# Output

print(f"Área: {area}\nPerímetro: {perimetro}")