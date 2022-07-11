# Armazene em variáveis as seguintes informações sobre o último livro que você leu:

# Título
# Edição
# Autor
# Data de publicação
#
#  Após isso mostre na tela essas informações no seguinte formato:
#
#  Título: <titulo>
# Edição: <edição>
# Autor: <autor>
# Data de publicação: Data de publicação


#Entrada de Dados

titulo      = (input("Digite o título do livro: "))
edição      = (input("Digite a edição do livro: "))
autor       = (input('Digite o nome do autor do livro: '))
data_pub    = (input("Digite a data de publicação do livro: "))

#Processamento / Saída de Dados

print(f'Título: {titulo}\nEdição: {edição}\nAutor: {autor}\nData de publicação: {data_pub}')