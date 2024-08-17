# Example Python script with various bugs and bad practices

import random

# Function 1: Simple syntax error, bad variable naming, and an unused variable
def bad_func_1():
    x = 10
    y == 20  # SyntaxError: should be '=' not '=='
    result = x + y
    unused_var = 5  # Unused variable
    print(f"Result is: {result}")

# Function 2: Division by zero, type error, and improper exception handling
def bad_func_2():
    try:
        num1 = 10
        num2 = "0"  # TypeError: Attempt to divide by a string
        result = num1 / int(num2)  # Potential ZeroDivisionError
    except:
        print("An error occurred")  # Bad practice: Catching all exceptions
    return result  # UnboundLocalError: result may not be defined

# Function 3: Infinite loop, mutable default argument, and poor efficiency
def bad_func_3(data=[]):
    while True:
        data.append(random.randint(1, 100))
        if len(data) > 10:
            break  # This loop is inefficient and has a potential memory leak
    return data

# Function 4: Race condition, global variable misuse, and unsecure random generation
global_counter = 0

def bad_func_4():
    global global_counter
    for _ in range(1000000):
        global_counter += random.randint(0, 1)  # Race condition in a multi-threaded context

    if global_counter == 500000:
        print("Halfway there!")  # Highly unlikely and misleading print statement

# Function 5: SQL Injection vulnerability and not using parameterized queries
def bad_func_5(user_input):
    query = f"SELECT * FROM users WHERE username = '{user_input}'"  # SQL Injection vulnerability
    print(f"Executing query: {query}")
    # Execution of the query is omitted, but this is where the risk lies

# Function 6: Memory leak, excessive recursion, and lack of input validation
def bad_func_6(n):
    if n == 0:
        return 0
    return n + bad_func_6(n - 1)  # No base case for large n, leading to maximum recursion depth error

# Function 7: Misuse of list comprehensions, and shadowing built-in functions
def bad_func_7(input_list):
    max = lambda x, y: x if x > y else y  # Shadowing built-in 'max' function
    return [max(i, 0) for i in input_list if max(i, 0)]  # Misuse: filtering twice with the same condition

# Function 8: Unsafe eval usage and potential code injection
def bad_func_8(user_code):
    try:
        result = eval(user_code)  # Extremely dangerous: allows code injection
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

# Function 9: Using deprecated libraries and functions
import imp  # Deprecated in favor of 'importlib'

def bad_func_9(module_name):
    try:
        module = imp.load_module(module_name, *imp.find_module(module_name))  # Deprecated approach
        print(f"Loaded module: {module}")
    except ImportError:
        print(f"Failed to load module: {module_name}")

# Function 10: Logic error and incorrect use of 'and'/'or'
def bad_func_10(a, b, c):
    if a and b or c:  # Misleading logic: could cause unintended outcomes
        print("Condition met")
    else:
        print("Condition not met")
