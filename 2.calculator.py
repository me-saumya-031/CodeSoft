import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error, Division by zero."
    else:
        return x / y

def square_root(x):
    return math.sqrt(x)

def percentage(x, y):
    return (x / y) * 100

def display_menu():
    print("\nSimple Calculator")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Percentage")
    print("7. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice in ['1', '2', '3', '4', '6']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(str(num1) + " + " + str(num2) + " = " + str(add(num1, num2)))
                elif choice == '2':
                    print(str(num1) + " - " + str(num2) + " = " + str(subtract(num1, num2)))
                elif choice == '3':
                    print(str(num1) + " * " + str(num2) + " = " + str(multiply(num1, num2)))
                elif choice == '4':
                    print(str(num1) + " / " + str(num2) + " = " + str(divide(num1, num2)))
                elif choice == '6':
                    print(str(num1) + " is " + str(percentage(num1, num2)) + "% of " + str(num2))
            elif choice == '5':
                num = float(input("Enter number: "))
                print("Square root of " + str(num) + " = " + str(square_root(num)))
        elif choice == '7':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

main()
