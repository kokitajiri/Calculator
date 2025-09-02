num1 = float(input("Please enter the first number:"))
cal = input("Please enter one of '+', '-', '*', or '/':")
num2 = float(input("Please enter the second number:"))
if cal == '+':
    num3 = num1 + num2
elif cal == '-': 
        num3 = num1 - num2
elif cal == '*': 
        num3 = num1 * num2
elif cal == '/': 
        num3 = num1 / num2
print("The answer is",num3)
