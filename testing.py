import unittest
from main import Calculator
import time


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_time1(self):
        t0 = time.time()
        print("System time is " + str(t0) + " seconds")

    def test_add(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(1, 2, 3).value, calc_value + 6)

    def test_mul(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 900)

    def test_divide(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.divide(2, 3).value, calc_value / 6)

    def test_divide_zero(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.divide(0).message, "Error")

    def test_pow(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(2, 3).value, (calc_value ** 2) ** 3)

    def test_pow_large(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(12).value, calc_value ** 12)

    def test_pow_zero(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(0).value, 1)

    def test_pow_less_zero(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(-5).value, 1.0 / (calc_value ** 5))

    def test_pow_rational(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(3.14).value, calc_value ** 3.14)

    def test_pow_incorrect_input(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power("MAAD").message, "Error")

    def test_root(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(25).value, calc_value ** 0.04)

    def test_root_zero(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(0).message, "Error")

    def test_root_less_zero(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(-10).value, 1.0 / calc_value ** 0.1)

    def test_root_rational(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(2.7).value, calc_value ** (1.0 / 2.7))

    def test_root_large(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(1000).value, calc_value ** 0.001)

    def test_multy_test1(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(30, 239).divide(20, 30, integer_divide=False).
                         power(7, 8, 350).subtract(1000000).value,
                         ((((calc_value + 269) / 600.0) ** 7) ** 8) - 1000000)

    def test_multy_test2(self):
        self.calculator = Calculator()
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(3, 5).multiply(10, 20, 30).subtract(10, 100, 1000000).power(4).value,
                         ((((calc_value ** (1.0 / 3.0)) ** (1.0 / 5.0)) * 6000.0) - 1000110) ** 4)

    def test_time2(self):
        t1 = time.time()
        print("System time is " + str(t1) + " seconds")


if __name__ == '__ main__':
    unittest.main()
