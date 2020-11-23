import art
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-":subtract,
    "*": multiply,
    "/": divide,
}

print(art.logo)
def calculator():
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)

    should_continue = True
    while should_continue:
        operation = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation]
        answer = calculation_function(num1,num2)


        print(f"{num1} {operation} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}: " ) == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
