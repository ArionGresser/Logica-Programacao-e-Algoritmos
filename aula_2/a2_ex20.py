# Construa um script que leia o preço de um produto, o percentual de desconto e calcule o valor a pagar e o valor do desconto.
# Entrada: 10
# 10
# Saída:
# Total = 9
# Desconto = 1


product_price  = float(input("Type the product price: "))
discount       = int(input("Type the discount: "))
total_discount = (product_price * (discount / 100))
total_price    = (product_price - total_discount)


print("Sub Total:", product_price)
print("Total: ", total_price)
print("Discount: ", total_discount)