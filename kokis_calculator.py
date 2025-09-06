import math

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





class FactorialCalc():
    def __init__(self, number=None):
        self.number = number
        self.answer = None
        
    def enter_number(self):
        while True:
            try:
                num = int(input("Please enter a positive integer:"))
                if num < 0:
                    print("The factorial of a negative number is undefined.")
                    continue
                self.number = num
                return num
            except ValueError:
                print('Please enter the correct number.')
                
    def factorial_calculate(self):
        if self.number == 0 or self.number == 1:
            self.answer = 1
            return 1
            
        else:
            result = 1
            for fac in range(2, self.number + 1):
                result *= fac
            self.answer = result
            return result





class PythagorasCalc():
    def __init__(self, side1_length=None, side2_length=None):
        self.side1_length = side1_length
        self.side2_length = side2_length
        self.answer = None
        
    def enter_side1(self):
        while True:
            try:
                side1 = float(input("Please enter the first length of side:"))
                if side1 <= 0:
                    print("Please enter the correct length of side.")
                    continue
                self.side1_length = side1
                return side1
            except ValueError:
                print("Please enter the correct length of side.")
            
    def enter_side2(self):
        while True:
            try:
                side2 = float(input("Please enter the second length of side:"))
                if side2 <= 0:
                    print("Please enter the correct length of side.")
                    continue
                self.side2_length = side2
                return side2
            except ValueError:
                print("Please enter the correct length of side.")
            
    def pythagoras_calculate(self):
        number1 = self.side1_length ** 2
        number2 = self.side2_length ** 2
        number3 = number1 + number2
        self.answer = math.sqrt(number3)
        return self.answer
        
        
        
        
        
def main():
    while True:
        print("1. Calculator with four functions.(+, -, *, /)")
        print("2.Factorial Calculator.")
        print("3.Pythagoras Calculator.")
        
        select = input("select an option (1-3):")
    
        if select == "1":
            calc = Calc()                   
            calc.enter_number1()            
            calc.enter_operator()           
            calc.enter_number2()            
            result = calc.calculate()      
            print("The answer is",result) 
        
        elif select == "2":
            calc = FactorialCalc()
            calc.enter_number()
            result = calc.factorial_calculate()
            print("The answer is", result)
        
        elif select == "3":
            calc = PythagorasCalc()
            calc.enter_side1()
            calc.enter_side2()
            result = calc.pythagoras_calculate()
            print("The length of the hypotenuse is", result)
            break
        
        else:
            print("Please enter the correct number.")
        
if __name__ == "__main__":
    main()
