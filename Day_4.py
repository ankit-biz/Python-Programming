#############################FUNCTION############################
''' Function is a set of code, which ones created, they can be used throughout program
Functions allow you to break down your code into smaller, manageable,
and reusable pieces, which makes your code more modular and easier to understand.'''
'''Advantage Why Use Functions?
Avoid code repetition
Increase readability and modularity
Easier debugging and maintenance.'''

# Types of functions
'''
1. Built-in Functions
These are pre-defined functions in Python that perform common operations.

Examples: print(), len(), type(), input(), sum(), max(), min(), etc.

2. User-Defined Functions
Functions created by users to perform specific tasks.

def greet(name):
    return f"Hello, {name}!"
print(greet("Ankit"))

3. Anonymous (Lambda) Functions
Functions without a name, usually used for short, single-line expressions.

square = lambda x: x * x
print(square(5))  # Output: 25

4. Recursive Functions
Functions that call themselves to solve a problem.

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  # Output: 120

5. Higher-Order Functions
Functions that take other functions as arguments or return functions. Examples: map(), filter(), reduce()

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

6. Generator Functions
Functions that yield values using yield, allowing iteration without storing all values in memory.

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
gen = count_up_to(3)
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

7. Decorator Functions
Functions that modify other functions without changing their structure.

def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()'''
# ----------------------------------------------------------------------------------------------------------------
# Basic Syntax of user defined function:
# def function_name(parameters):
#            """Docstring (optional)"""
#                # Function body
#            return value  # Optional

def one():
    print("First Function")
one()

def mul():
    a=21
    b=9
    print(a*b)
mul()

def name():
    print("this is the new beginning")

# Different ways for creating a user-defined functions
#----------------------1. Function Arguments (Parameters)-----------------------
# Functions can accept arguments (inputs) to perform operations. Python supports several types of arguments:
'''Types of Function Arguments
1️⃣ Positional Arguments
2️⃣ Keyword Arguments
3️⃣ Default Arguments
4️⃣ Variable-Length Arguments (*args, **kwargs)'''

'''parameter: Parameters are the variables listed inside the parentheses in the function definition.
They act as placeholders for the values that will be passed to the function when it is called.'''
# a. Positional Arguments -> Arguments are passed in the order they are defined.
def add_numbers(a, b):  # a and b are parameters
    return  a+b

la=add_numbers(2,4)     #   Correct: Pass two positional -> 2, 4 are argunments values
print(la)
print(add_numbers(23,2))

# b. Keyword Arguments  ->
def ka(nickname,name):
    print(f"You know i have two name first one my documented name is \"{name}\" and another name that my family call me it is \"{nickname}\"")

ka(name='Ankit Verma',nickname='Anurag')      # Keyword arguments

# c. Default Arguments
def da(naam="King"):        # default algument (naam="King")
    print(f"hello {naam}")

da()
print(da("Kaam"))  # Overrides default value
#------------------------------------------------------
def greet(name, message="Hello"):       # Default arguments should always be at the end!
    print(f"{message}, {name}!")
greet("Alice")  # Uses default message: "Hello"
greet("Bob", "Hi")  # Overrides default message

#----------------------------2. Variable-Length Arguments (*args and **kwargs)---------------------------
'''Functions can accept a variable number of arguments using *args (arbitrary for positional arguments) and **kwargs (arbitrary for keyword arguments).
*args: Collects extra positional arguments as a tuple.
**kwargs: Collects extra keyword arguments as a dictionary.'''
def sum_all(*args):
    print(sum(args))
sum_all(23,23,45,55,23,45)        # Pass multiple arguments

def display_info(**kwargs):
    print(kwargs)
display_info(name="Sheetal Mata", age=3)

def display_info1(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
display_info1(name="Sheetal Mata", age=3, city="Noida")

def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_args(1, 2, 3, name="Alice", age=25)   # Keyword arguments: {'name': 'Alice', 'age': 25} # Positional arguments: (1, 2, 3)

def arbutaryarguments(*name):
    print("my name is", name[2])
arbutaryarguments("Ankit", "Ashok","Nagar")

'''Arguments are the actual values you pass to the function when you call it.
These values are assigned to the corresponding parameters defined in the function.'''

result = add_numbers(3, 5)  # 3 and 5 are arguments
print(result)

#-----------------------3. Return Statement / Returning Values from Functions-----------------------
'''retuen keyword used to exit a function and return the value of a function. If no return statement is provided, the function returns None.'''
def aoke():
    return "Hi! how can i help you?"
print(aoke())

def RS(a,b):
    return a+b
print(RS(12,2))

def MRV(a,b):        #Multiple Return Values. Python functions can return multiple values as a tuple.
    return a + b, a - b, a * b
add, diff, mul= MRV(12,44)
print(add,diff,mul)

def none():         #A function without a return statement returns None:
    pass

#--------------------------4. Scope of Variables (Local vs. Global)-------------------------
#Local Scope (Inside the Function)--> A local variable is created inside a function and only accessible within that function.
#Global Scope (Outside the Function)--> A global variable is declared outside the function and can be accessed anywhere.
def area_of_circle(r):
    pie=22/7           # local variable
    print(f"pie: {pie} * {r}*{r} and  and sum is -> {pie*(r**2)}")
area_of_circle(5)
# -------------------------------------------------------------

boxer = 232   # global variable
def global_var_Exa():
    print(boxer)        # Accessing global variable
global_var_Exa()
print(boxer)        # Accessible outside function too

#c. Modifying a Global Variable Inside a Function:
def modify_gv():
    global boxer     # Use global keyword to modify
    boxer +=68
    print(boxer)
modify_gv()         # output boxer=300
print(boxer)        # Now the value is changed

#d. Nonlocal Variables The nonlocal keyword is used to modify a variable in the nearest enclosing scope
def outer_function():
    bud = 23  # Enclosing scope variable (defination: variable defined in an outer function that is accessible inside an inner (nested) function.)

    def inner_function():
        nonlocal bud
        bud = 240  # Modifying enclosing scope variable

    inner_function()
    print(bud)

outer_function()

#---------------------------5. Nested Functions & Closures--------------------------
# A nested function is a function defined inside another function. Inner functions retaining access to outer function’s scope.
def outer_function1():
    message = "Hello"

    def inner_function1():
        print(message)  # Accessing variable from outer function

    inner_function1()  # Calling inner function

outer_function1()

#-------------------------------------6. Recursion Function-------------------------
'''A recursion function is a function that calls itself in order to solve a problem.
Key Concepts in Recursion
1. Base Case->  Definition: The condition under which the recursion stops. Purpose: Prevents infinite recursion by providing a terminating scenario.
2. Recursive Case-> Definition: The part of the function where it calls itself with a modified argument. Purpose: Breaks the problem into smaller instances of the same problem.'''
i=0
def recur():        # default limit of calling recursion is 1000 in python
    global i
    i += 1
    print("I am millionaire",i)
    recur()         # a function is called by itself
recur()

# Factorial
def fact(n):
    if n==0 or n==1:    # Base Case
        return 1
    else:
        return n*fact(n-1)      # Recursive Case
print(fact(3))

# fibonacci series
def fibonacci(n):
    if n <= 0:  # Base case for non-positive n
        return 0
    elif n == 1:  # Base case for n equal to 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Testing the fibonacci function
print(fibonacci(10))  # Output: 55


#------------------------------------7. Lamda Function---------------------------
'''lamda function used when anonymus function is required for a short period of time. A lambda function is a small anonymous function with no def keyword.'''
# They are often used as arguments to higher-order functions like map(), filter(), and reduce().
# SYNTAX: lambda arguments: expression
sumittion= lambda a: a**2
print(sumittion(4))

u= lambda b1,b2,b3: b2*(b1+b3)
print(u(2,3,5))

# finding no. is even or odd
m= lambda x : "Even" if x%2==0 else "Odd"
print(m(39))

# maximum no. in between two numbers
o=lambda x,y: x if x > y else y
print(o(24,43))

# maximum no. in between three numbers
cz=lambda d,g,t:d if d>g and d>t else(g if g>t else t)
print(cz(3,143,65))

# using map for iterate each element of list
sd=[4,6,87,3]
square=list(map(lambda x : x**2,sd))
print(square)

# using filter to extract even number from the list
de=[4,23,67,98,123]
even=list(filter(lambda x : x % 2 == 0,de))
print(even)

# calculator using lambda function
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "Cannot divide by zero"
}

print(operations["add"](10, 5))       # Output: 15
print(operations["multiply"](6, 7))   # Output: 42

# Use lambda with sorted() to sort a list of students by name length.
students = ["Ankit", "Ravi", "Amitabh", "Raj"]
sorted_students = sorted(students, key=lambda x: len(x))
print(sorted_students)  # Output: ['Raj', 'Ravi', 'Ankit', 'Amitabh']

# --------------------------------------------8.Docstrings---------------------------------------------
'''
Docstrings are a fundamental part of Python programming, enabling you to document your code effectively.
They improve readability, support maintenance'''
# Example 1
def greet(name):
    """Return a personalized greeting message."""       #-> DOCSTRINGS
    return f"Hello, {name}!"
print(greet("Gola Bulia"))
# Example 2
def adda(a, b):
    """Add two numbers and return the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b

#--------------------------------------9. Error Handling in functions----------------------------
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        # Handle specific error: division by zero.
        print(f"Error: Cannot divide by zero. Details: {e}")
        result = None  # Or choose to return a default value
    except Exception as e:
        # Catch any other unexpected exceptions.
        print(f"An unexpected error occurred: {e}")
        result = None
    else:
        # Executes if no exception is raised in the try block.
        print("Division successful.")
    finally:
        # This block always executes, regardless of exceptions.
        print("Exiting divide_numbers function.")
    return result

# Example usage:
print(divide_numbers(10, 2))  # Expected output: 5.0 and messages.
print(divide_numbers(10, 0))  # Expected output: None with an error message.


#-------------------------------------10. Higher-Order Functions (Functional Programming)---------------------------------------------
# A higher-order function is a function that takes another function as an argument.

# 1. map() – Apply a Function to All Elements and applies a function to every element of an iterable (list, tuple, etc.).
# Example a: Square Each Element
lota=[12,3,4,64,5]
square=list(map(lambda x: x**2,lota))
print(square)

# Example b: Convert List of Strings to Uppercase
chota=["raghav","kshitij","vishnu","kaalu"]
uper=list(map(lambda w:w.upper(),chota))
######problem solving

# 2. filter() – Filter Elements Based on a Condition
# Example a: Get Even Numbers
even=list(filter(lambda x:x%2==0,lota))
print(even)

# Example b: Filter Names with Length > 4
length=list(filter(lambda x:len(x)>4,chota))
print(length)

# 3. reduce() – Reduce an Iterable to a Single Value
# The reduce() function applies a function cumulatively to the elements of an iterable.
from functools import reduce

numbers = [4, 8, 2, 10, 5]
max_num = reduce(lambda x, y: x if x > y else y, numbers)

print(max_num)  # Output: 10

#-----------------------------------------------------Decorator---------------------------------------------------------
'''A decorator is a function that takes another function as an argument, extends or modifies its behavior, and returns a new function.
Decorators leverage Python's ability to treat functions as first-class objects, meaning functions can be:
1. Assigned to variables,
2. Passed as arguments to other functions,
3. Returned from functions.

This property is the foundation of how decorators work. The decorator "wraps" the original function, allowing you to 
execute additional code before or after the original function runs.
The syntax for applying a decorator uses the @ symbol above a function definition, making code cleaner and more 
readable compared to manually applying the wrapper.
'''
# example 1
def decorator(func):
    def wrapper():
        print(f"Good morning")
        func()
        print("Thank you for connecting us")
    return wrapper()
@ decorator # write this before the origional one for calling decorator function
def orignal():
    print(f"How can i help you? ")
# decorator(orignal) # manually calling the decorator function

# example 2
def dec(func):
    def execute(**kwargs):
        print("Good Morning")
        func(**kwargs)  # Pass the arguments to func
        print("Nice to meet you")
    return execute  # Return the function not the result

@dec
def my(name):
    print(f"Hi {name}, how can I help you?")

my(name="hhh")

# Multiple decoration
def deco_Uppercase(func):
    def wrapper():
        result = func().upper()
        return result
    return wrapper

def deco_split(func):
    def wrapper():
        result = func().split()
        return result
    return wrapper

@deco_split
@deco_Uppercase
def naam_daal():
    i=input("Enter first name: ")
    j=input("Enter Last name: ")
    full_name=i+" "+j
    return full_name

print(naam_daal())

# Tough 🙂
from datetime import datetime
def deco(func):
    def wrapper(*args):
        result = func(*args)
        print(f"Your Birth Year was {result}")
        year = datetime.now().strftime("%Y")
        print(f"Current year is {year}")
    return wrapper

@deco
def birt_year():
    i=int(input("Enter your DOB year as \"YYYY\"-> "))
    return i

birt_year()

#waf to find maximum of three numbers
def max(a,b,c):
    if a>b and a>c:
        return (a)
    elif b>c and b>a:
        return (b)
    else:
        return (c)

print("Largest number is",max(2,4,6))

#--------------------------------------------Generators---------------------------------------------
'''A generator function in Python is a special type of function that uses the yield keyword to produce a sequence of values lazily, 
i.e., one at a time, rather than computing and returning them all at once. When called, a generator function does not execute its body
 immediately; instead, it returns a generator object, which is an iterator that can be used to retrieve values on demand.'''
# 1. Iterator Protocol: Generator objects implement the iterator protocol with __iter__() and __next__() methods.
# 2. Generator functions are defined using the def keyword, just like regular functions, but they include at least one yield statement.
#     The presence of yield transforms the function into a generator function.
# 3. The yield Keyword: The Heart of Generators
# 4. Use yield to produce a series of values over time. They return a generator object which is an iterator.

def gen(n):
    i=0
    while i<n:
        yield i
        i+=1
a = gen(10)       # Create a generator object
print(next(a))      # 1
print(next(a))      # 2
print(next(a))      # 3
print(list(a))      # all data

'''for i in a:         # printing all using loop
    print(i)'''

# Single iteration Or exhaustion
def gen_three():
    yield 1
    yield 2
    yield 3

gen = gen_three()
print(list(gen))  # [1, 2, 3]
print(list(gen))  # []

# Lazy Evaluation
def lazyGen():
    n=0
    while True:
        yield n
        n +=1
a=lazyGen()
print(next(a))
#-------------------------------Creating and Importing Modules---------------------------------
# 1. fist create a file. now i'm creating module name file.
# 2. after that write a funtions or anything that you want.
# 3. import the file where you want

# 4. Use the import statement to use the module in another script.
import module           # using that import all over the module
from module import add,mul  # Importing Specific Functions, not all the module  (from ... import ....)
import module as my     # Importing with Aliases. Use aliases to shorten module or function names.
module.mul(24,23)  # 5 calling it firstly write the module name and using '.' write the function that you want to call.

#------------------------------Creating and Importing Packages--------------------------------------
'''A package is a directory containing an __init__.py file and one or more modules.

a. Creating a Package
Create a directory (e.g., mypackage).

Add an __init__.py file (can be empty or contain initialization code).

Add modules to the directory.'''
