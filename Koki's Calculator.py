while True:
    try:
        number1 = float(input("Please enter the first number:"))
        break
    except ValueError:
        print("Please enter the correct number.")

while True:
    calculator = input("Please enter one of '+', '-', '*', or '/':")
    if calculator in ['+', '-', '*', '/']:
        break

    else:
        print("Please enter the correct operator.")

while True:
    try:
        number2 = float(input("Please enter the second number:"))
        if calculator == '/' and number2 == 0:
            print("You can't divide by 0")
            continue
        break
    except ValueError:
        print("Please enter the correct number.")

if calculator == '+':
    number3 = number1 + number2
elif calculator == '-': 
    number3 = number1 - number2
elif calculator == '*': 
    number3 = number1 * number2
elif calculator == '/': 
    number3 = number1 / number2
print("The answer is",number3)

