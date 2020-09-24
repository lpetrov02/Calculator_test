import math
import random
import time


class Calculator:
    def __init__(self):
        self.value = random.randrange(1, 1000, 1)
        self.message = ""

    def add(self, *args):
        if type(sum(args)) != int and type(sum(args)) != float:
            self.message = "Error"
            return self
        self.value += sum(args)
        return self

    def multiply(self, *args):
        for x in args:
            if type(x) != int and type(x) != float:
                self.message = "Error"
                return self
            self.value *= x
        return self

    def power(self, *args):
        i = 0
        for x in args:
            if i > 1:
                return self
            if type(x) != int and type(x) != float:
                self.message = "Error"
                return self
            self.value **= x
            i += 1
        return self

    def divide(self, *args, integer_divide=False):
        for x in args:
            if type(x) != int and type(x) != float or x == 0:
                self.message = "Error"
                return self
            if integer_divide:
                self.value //= x
            else:
                self.value /= x
        return self

    def subtract(self, *args):
        if type(sum(args)) != int and type(sum(args)) != float:
            self.message = "Error"
            return self
        self.value -= sum(args)
        return self

    def root(self, *args):
        for x in args:
            if x == 0 or type(x) != int and type(x) != float:
                self.message = "Error"
                return self
            self.value **= 1/x
        return self

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    calculator = Calculator()
    print(calculator)
    print(calculator.add(1, 2, 3, 5.1).multiply(4, 0.123).subtract(4, 1, -100).divide(5, integer_divide=True))
    print(calculator.value + 10)
    print(10 + calculator.value)
