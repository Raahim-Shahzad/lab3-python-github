def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
def calculate_percentage(number, total):
    if total == 0:
        return "Error: Cannot calculate percentage when the second number is zero."
    return (number / total) * 100

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    while True:
        print("\n===== PYTHON CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Check Even/Odd")
        print("6. Calculate Percentage")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            print("Result:", addition(a, b))
        elif choice == "2":
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            print("Result:", subtraction(a, b))
        elif choice == "3":
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            print("Result:", multiplication(a, b))
        elif choice == "4":
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            print("Result:", division(a, b))
        elif choice == "5":
            number = get_number("Enter a whole number: ")
            if not number.is_integer():
                print("Please enter a whole number.")
            else:
                print(
                    f"{int(number)} is",
                    check_even_odd(int(number))
                )
        elif choice == "6":
            number = get_number("Enter the number to calculate: ")
            total = get_number("Enter the total/reference number: ")
            result = calculate_percentage(number, total)

            if isinstance(result, str):
                print(result)
            else:
                print(f"Percentage: {result:.2f}%")
        elif choice == "7":
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option from 1 to 7.")

if __name__ == "__main__":
    main()
