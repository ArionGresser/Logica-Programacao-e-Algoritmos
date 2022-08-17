# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). 
# Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
# Entrada:
# João
# 500
# 1230.3
# Saída:
# Total = R$ 684.54


# employee comission = 15%
employee_name   = str(input("Type the employee name: "))
salary_settled  = float(input("Type the empolyee salary: "))
sales           = float(input("Type the empolyee sales: "))
total_salary    = (salary_settled + sales * 0.15)


print("Employee:", employee_name)
print(f"Salary to pay: $ {total_salary:.2f}")


