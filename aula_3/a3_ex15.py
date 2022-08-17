# Leia o salario de um trabalhador e o valor da prestação de um empréstimo. 
# Se a prestaçao for maior que 20% do salário imprima: “empréstimo não concedido”,
#  caso contrario imprima: “empréstimo concedido”.


salary                 = float(input("Type your salary: "))
installment            = float(input("Type a installment value: "))
salary_porcentage      = (salary * 0.2)

if installment <= salary_porcentage:
    print("Loan granted!")
elif installment > salary_porcentage:
    print("Loan not granted.")