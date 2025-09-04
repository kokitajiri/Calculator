import math

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
    calc = PythagorasCalc()
    calc.enter_side1()
    calc.enter_side2()
    result = calc.pythagoras_calculate()
    print("The length of the hypotenuse is", result)
    
if __name__ == "__main__":
    main()
