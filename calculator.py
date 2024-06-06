# Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print(e)

# Function to perform exponentiation
def power(a, b):
    return a ** b

# Function to perform remainder calculation
def remainder(a, b):
    return a % b

# Function to handle arithmetic operations
def select_op(choice):
    if choice == '#':
        return -1
    elif choice == '$':
        return 0
    elif choice in ('+','-','*','/','^','%'):
        while True:
            num1s = str(input("Enter first number: "))
            print(num1s)
            if num1s.endswith('$'):
                return 0
            if num1s.endswith('#'):
                return -1
            try:
                num1 = float(num1s)
                break
            except:
                print("Not a valid number, please enter again")
                continue
        
        while True:
            num2s = str(input("Enter second number: "))
            print(num2s)
            if num2s.endswith('$'):
                return 0
            if num2s.endswith('#'):
                return -1
            try:
                num2 = float(num2s)
                break
            except:
                print("Not a valid number, please enter again")
                continue
        
        result = 0.0
        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            result = remainder(num1, num2)
        else:
            print("Something Went Wrong")
        
        # Format the calculation for history
        last_calculation = "{0} {1} {2} = {3}".format(num1, choice, num2, result) 
        print(last_calculation)

        # Append the calculation to the history list
        history.append(last_calculation)

    elif choice == '?':
        if not history:
            print("No past calculations to show")
        else:
            for calc in history:
                print(calc)
    else:
        print("Unrecognized operation")

# Main loop
history = []  # List to store the history of calculations
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")

    # Take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    if select_op(choice) == -1:
        # Program ends here
        print("Done. Terminating")
        exit()
