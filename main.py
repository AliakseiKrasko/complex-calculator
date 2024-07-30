from complex_number import ComplexNumber
from calculator import Calculator
from logger import setup_logger

def main():
    logger = setup_logger()
    calculator = Calculator(logger)

    num1 = ComplexNumber(2, 3)
    num2 = ComplexNumber(1, 4)

    result_add = calculator.add(num1, num2)
    result_multiply = calculator.multiply(num1, num2)
    result_divide = calculator.divide(num1, num2)

    print(f"Addition: {result_add}")
    print(f"Multiplication: {result_multiply}")
    print(f"Division: {result_divide}")

if __name__ == "__main__":
    main()
