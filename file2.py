import time
import os
import math

# Function 11: Unnecessary complexity, redundant code, and poor readability
def bad_func_11(x):
    if x > 0:
        if x > 10:
            if x > 20:
                return x * 2
            else:
                return x * 2  # Redundant condition, unnecessary nesting
        else:
            return x * 2
    else:
        return x * 2

# Function 12: Hardcoded values, magic numbers, and lack of documentation
def bad_func_12():
    num = 12345
    result = num % 7  # Magic number '7' without explanation
    if result == 0:
        print("Number is divisible by 7")
    else:
        print("Number is not divisible by 7")
    return result

# Function 13: Incorrect use of try-except, and ignoring exceptions
def bad_func_13():
    try:
        f = open('non_existent_file.txt', 'r')
    except IOError:
        pass  # Ignoring the exception silently
    finally:
        f.close()  # UnboundLocalError: f may not be defined

# Function 14: Improper use of threads, leading to a deadlock
from threading import Thread, Lock

lock1 = Lock()
lock2 = Lock()

def thread1():
    lock1.acquire()
    time.sleep(0.1)
    lock2.acquire()  # Potential deadlock if thread2 acquires lock2 first

def thread2():
    lock2.acquire()
    time.sleep(0.1)
    lock1.acquire()  # Potential deadlock if thread1 acquires lock1 first

def bad_func_14():
    t1 = Thread(target=thread1)
    t2 = Thread(target=thread2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# Function 15: Unhandled exceptions, division by zero, and misuse of assertions
def bad_func_15(x):
    assert x != 0, "x cannot be zero"  # Misuse of assertion for input validation
    return 10 / x  # Potential ZeroDivisionError if x is zero

# Function 16: Resource leak, unclosed file handle, and non-idiomatic code
def bad_func_16():
    f = open('somefile.txt', 'w')
    f.write('Hello, World!')
    # File handle is not closed; resource leak occurs

# Function 17: Incorrect use of recursion, exceeding maximum recursion depth
def bad_func_17(x):
    if x <= 1:
        return 1
    else:
        return x * bad_func_17(x + 1)  # This will cause a RecursionError for large x

# Function 18: Mismanagement of mutable data structures, causing unintended side effects
def bad_func_18(lst=[]):
    lst.append(1)  # Mutable default argument
    return lst

# Function 19: Race condition due to improper locking mechanism
def bad_func_19():
    total = 0
    def add_to_total(n):
        nonlocal total
        for _ in range(n):
            total += 1  # Race condition in a multi-threaded environment

    threads = []
    for _ in range(10):
        t = Thread(target=add_to_total, args=(100000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Total: {total}")

# Function 20: Buffer overflow vulnerability (simulated in Python)
def bad_func_20(data):
    buffer = [0] * 10  # Fixed-size buffer
    for i in range(len(data)):
        buffer[i] = data[i]  # No bounds checking, potential overflow if len(data) > 10

# Function 21: Inconsistent data handling, leading to potential data corruption
def bad_func_21():
    data = {"key1": 10, "key2": 20}
    for key in data.keys():
        data[key] += data.get(key, 0)  # Redundant and confusing operation

    if "key3" not in data:
        data["key3"] = 0  # Inconsistent state; unexpected behavior later
    return data

# Function 22: Overly complex conditional logic, leading to difficult maintenance
def bad_func_22(a, b, c):
    if (a > b and b < c) or (a < b and b > c):
        if not (a == b or b == c):
            return (a + b) * c
    else:
        return (a - b) / (c + 1)  # Complex and difficult to understand logic

# Function 23: Memory exhaustion, creating unnecessary large data structures
def bad_func_23():
    large_list = [x for x in range(100000000)]  # Creates a huge list, leading to potential memory issues

# Function 24: Time of check to time of use (TOCTOU) race condition
def bad_func_24(filename):
    if os.path.exists(filename):
        f = open(filename, 'w')  # TOCTOU: file could be modified/deleted before opening
        f.write("New content")
        f.close()

# Function 25: Incorrect variable scoping, leading to unexpected behavior
def bad_func_25():
    for i in range(5):
        j = i * 2
    print(j)  # Variable 'j' is not defined outside the loop in some languages, but here it could be misused

# Function 26: Hardcoding sensitive information and lack of encryption
def bad_func_26():
    api_key = "12345-abcde-67890-fghij"  # Hardcoded sensitive information
    print(f"API Key: {api_key}")  # Exposing sensitive information

# Function 27: Overuse of global variables, leading to spaghetti code
global_var = 10

def bad_func_27():
    global global_var
    global_var += 5
    print(f"Global variable is now {global_var}")

# Function 28: Confusing use of nested ternary operators
def bad_func_28(a, b, c):
    result = a if a > b else b if b > c else c  # Hard to read and maintain
    return result

# Function 29: Inefficient search algorithm, O(n^2) complexity instead of O(n log n)
def bad_func_29(lst, target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == target or lst[j] == target:
                return True
    return False  # This could be done in O(n log n) with a sorted list and binary search

# Function 30: Incorrect string formatting leading to runtime errors
def bad_func_30(name, age):
    print("Name: %s, Age: %d" % (name, age))  # %d expects an integer, will break if age is not an int

# Function 31: Floating point precision issues
def bad_func_31():
    a = 0.1
    b = 0.2
    c = 0.3
    if a + b == c:  # Will not be true due to floating point precision errors
        print("Correct")
    else:
        print("Incorrect")

# Function 32: Inefficient and redundant code with nested loops
def bad_func_32(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] == lst[j] and i != j:
                return True  # This could be done more efficiently
    return False

# Function 33: Recursive function without proper termination leading to stack overflow
def bad_func_33(n):
    if n == 1:
        return 1
    else:
        return n * bad_func_33(n)  # This should reduce n but doesn't, causing infinite recursion

# Function 34: Misuse of lambda functions, leading to confusing code
def bad_func_34(x):
    return (lambda y: y + 1)(lambda z: z * 2)(x)  # Nested lambdas making code hard to understand

# Function 35: Overly complicated regex with potential for catastrophic backtracking
import re

def bad_func_35(text):
    pattern = re.compile(r"(a+)+b")  # Potential for catastrophic backtracking on certain input
    return pattern.search(text)

# Function 36: Lack of security in handling sensitive user input
def bad_func_36(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username}:{password}\n")  # Storing passwords in plain text is insecure

# Function 37: Poor use of exception handling, swallowing critical errors
def bad_func_37(x):
    try:
        result = math.sqrt(x)  # Will raise ValueError for negative x
    except:
        result = None  # Swallowing all exceptions is dangerous
    return result

# Function 38: Using eval for mathematical expression parsing (security risk)
def bad_func_38(expression):
    return eval(expression)  # Allows execution of arbitrary code, leading to security vulnerabilities

# Function 39: Unnecessarily complex and convoluted string manipulation
def bad_func_39(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].upper()
        else:
            result += s[i].lower()
    return result  # This could be done more efficiently with a list comprehension or generator

# Function 40: Incorrect file handling with no context manager
def bad_func_40():
    f = open('somefile.txt', 'w')
    try:
        f.write('Hello, World!')
    finally:
        f.close()  # File should be handled with a context manager to avoid resource leaks
