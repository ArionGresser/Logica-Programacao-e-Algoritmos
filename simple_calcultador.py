# ARION'S CALCULATOR
print("--------WELCOME TO THE ARION'S CALCULATOR--------")
n1 = float(input("Insert the first number for calculate: "))
n2 = float(input("Insert the second number for calculate: "))

operation = str(input("Insert (+) for Addition, (-) for Subtraction, (*) for Multiplication or (/) for Division: "))

if operation == "+":
    print("Result of Addition: "), print(n1 + n2), print("--------END--------");
elif operation == "-":
    print("Result of Subtraction: "), print(n1-n2), print("--------END--------");
elif operation == "*":
    print("Result of Multiplication: "), print(n1*n2), print("--------END--------");
elif operation == "/":
    print("Result of Division: "), print(n1/n2), print("--------END--------");
else:
    print("!! FATAL ERROR !! You isert an invalid input, verify the correct options and try again.");