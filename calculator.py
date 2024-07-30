from complex_number.py import ComplexNumber
import logging

class Calculator:
    def __init__(self, logger):
        self.logger = logger

    def add(self, num1, num2):
        result = ComplexNumber(num1.real + num2.real, num1.imag + num2.imag)
        self.logger.info(f"Added {num1} to {num2}, result is {result}")
        return result

    def multiply(self, num1, num2):
        real = num1.real * num2.real - num1.imag * num2.imag
        imag = num1.imag * num2.real + num1.real * num2.imag
        result = ComplexNumber(real, imag)
        self.logger.info(f"Multiplied {num1} by {num2}, result is {result}")
        return result

    def divide(self, num1, num2):
        denominator = num2.real ** 2 + num2.imag ** 2
        real = (num1.real * num2.real + num1.imag * num2.imag) / denominator
        imag = (num1.imag * num2.real - num1.real * num2.imag) / denominator
        result = ComplexNumber(real, imag)
        self.logger.info(f"Divided {num1} by {num2}, result is {result}")
        return result
