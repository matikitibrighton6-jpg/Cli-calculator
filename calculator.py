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


def menu():
    print("\n=== CLI Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    
history = []


while True:
    menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == '1':
            result = add(num1, num2)
            operation = "Addition"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "Subtraction"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "Multiplication"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "Division"
        
        print(f"{operation} Result: {result}")
        history.append(f"{operation}: {num1} and {num2} => {result}")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        
print("\n=== Calculation History ===")

memory = input("Show History? (y/n): ").lower()
if memory == 'y':
    for record in history:
        print(record)       