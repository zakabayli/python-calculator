import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    continue_calculating = True

    while continue_calculating:
        num1 = float(input("What is the first number?: "))
        
        for symbol in operations:
            print(symbol)
        should_continue = True

        while should_continue:
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What is the next number?: "))
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)

            print(f"{num1} {operation_symbol} {num2} = {answer}")

            choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start over, or 'q' to quit: ").lower()
            
            if choice == "y":
                num1 = answer
            elif choice == "n":
                should_continue = False  # Start over
            else:
                should_continue = False
                continue_calculating = False  # Exit the calculator

calculator()
