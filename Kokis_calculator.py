class Calc():
        #set up the class
    def __init__(self):
        self.number1 = None
        self.operator = None
        self.number2 = None
        
    #Ask user to enter the first number
    def enter_number1(self):
        while True:
            
            try:
                number1 = float(input("Please enter the first number:"))
                #If the input is correct, it is stored in num1.ope and returned.
                self.number1 = number1 
                return number1 
            except ValueError:
                print('Please enter the correct number.')
    
    #Ask user to enter the operator.
    def enter_operator(self):
        while True:
            operator = input("Please enter one of '+', '-', '*', or '/':")
            if operator in ['+', '-', '*', '/']:
                #If the input is correct, it is stored in self.ope and returned.
                self.operator = operator
                return operator
            else:
                #If tre operator is invalid, show error message
                print("Please enter the correct operator.")
    
    #Ask user to enter the second number.        
    def enter_number2(self):
        while True:
            try:
                number2 = float(input("Please enter the second number:"))
                if self.operator == '/' and number2 == 0:
                    print("You can't divide by 0.")
                    continue
                self.number2 = number2
                return number2
            except ValueError:
                print("Please enter the correct number.")
                
    def calculate(self):
        if self.operator == '+':
            return self.number1 + self.number2
        elif self.operator == '-':
            return self.number1 - self.number2
        elif self.operator == '*':
            return self.number1 * self.number2
        elif self.operator == '/':
            return self.number1 / self.number2

#Main function to run the calculator.
def main():
    calc = Calc()                   #Create a Calc object
    calc.enter_number1()            #Get the first number
    calc.enter_operator()           #Get the operator
    calc.enter_number2()            #Get the second number
    result = calc.calculate()       #Calculate result
    print("The answer is",result)   #Show the result

if __name__ == "__main__":
    main()
