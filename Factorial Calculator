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
        
def main():
    calc = FactorialCalc()
    calc.enter_number()
    result = calc.factorial_calculate()
    print("The answer is", result)

if __name__ == "__main__":
    main()
