from art import logo, clear_console


# Calculator
def add(a,b):
    return a+b

def substract(a, b):
    return a-b

def multiply(a, b):
    return a * b

def divide(a,b):
    return a / b

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    num1 = float(input("What's the First Number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the Next number?: "))
        function = operations[operation]
        answer = function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new  calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear_console()
            calculator()

calculator()


        
