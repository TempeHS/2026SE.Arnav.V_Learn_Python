num1 = int(input("Enter the first number: "))
Operator = input("Enter the operator: ")
num2 = int(input("Enter the second number: "))
if Operator == "+":
    print("The answer is: ", num1 + num2)
elif Operator == "-":
    print("The answer is: ", num1 - num2)
elif Operator == "*" or Operator == "x":    
    print("The answer is: ", num1 * num2)
elif Operator == "/":
    print("The answer is: ", num1 / num2)
else:
    print("Invalid operator")