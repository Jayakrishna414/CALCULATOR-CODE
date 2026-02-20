# Simple Python Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            if op == '+':
                print("Result:", add(num1, num2))
            elif op == '-':
                print("Result:", subtract(num1, num2))
            elif op == '*':
                print("Result:", multiply(num1, num2))
            elif op == '/':
                print("Result:", divide(num1, num2))
            else:
                print("Invalid operation!")
            
            again = input("Do you want to calculate again? (yes/no): ").lower()
            if again != "yes":
                print("Calculator closed.")
                break
        
        except ValueError:
            print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    calculator()
