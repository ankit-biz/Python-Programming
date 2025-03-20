#------------------------------Python Built-in Functions-------------------------------------
'''Python provides a rich set of built-in functions that can be used without needing to import any module.
These functions help perform various operations like data type conversions, mathematical calculations, input/output operations, and more.'''

#----------------1. Input/Output Functions
# a). print() – Display Output
print("Hello, World!")  # Output: Hello, World!
print(10, 20, 30, sep="-")  # Output: 10-20-30
print("Python", end="!")  # Output: Python!

# b). input() – Take User Input
name = input("Enter your name: ")       # Accepts input as a string by default.
print("Hello,", name)

age = int(input("Enter your age: "))  # Converts input to integer
print("Your age is:", age)

#-------------------------2. Type Conversion Functions
# -> These functions convert data from one type to another.
# a). int() – Convert to Integer
print(int(3.7))  # Output: 3
print(int("10"))  # Output: 10

# b). float() – Convert to Floating Point Number
print(float(5))  # Output: 5.0
print(float("3.14"))  # Output: 3.14

# c). str() – Convert to String
print(str(100))  # Output: '100'
print(str(3.14))  # Output: '3.14'

# d). bool() – Convert to Boolean
print(bool(0))  # Output: False
print(bool(10))  # Output: True
print(bool(""))  # Output: False

# e). list(), tuple(), set(), dict() – Convert to Respective Data
print(list("hello"))  # Output: ['h', 'e', 'l', 'l', 'o']
print(tuple([1, 2, 3]))  # Output: (1, 2, 3)
#print(set([1, 2, 3]))  # Output: {1, 2, 3}
print(dict([(1, 'a'), (2, 'b')]))  # Output: {1: 'a', 2: 'b'}

#---------------------------------- 3. Mathematical Functions
# a). abs() – Absolute Value
print(abs(-10))  # Output: 10
print(abs(3.5))  # Output: 3.5

# b). pow() – Power Calculation (x^y)
print(pow(2, 3))  # Output: 8 (2^3)
print(pow(5, 2))  # Output: 25 (5^2)

# c). round() – Round a Number
print(round(3.14159, 2))  # Output: 3.14
print(round(5.678))  # Output: 6 (default rounds to nearest integer)

# d). max() & min() – Find Maximum and Minimum
numbers = [10, 20, 5, 40]
print(max(numbers))  # Output: 40
print(min(numbers))  # Output: 5

# e). sum() – Sum of All Elements in an Iterable
print(sum([1, 2, 3, 4, 5]))  # Output: 15

#-------------------------------- 4. String Functions
# a). len() – Get Length of String or Collection
print(len("Python"))  # Output: 6
print(len([1, 2, 3, 4]))  # Output: 4

# b). ord() & chr() – Convert Characters to ASCII and Vice Versa
print(ord("A"))  # Output: 65 (ASCII value of 'A')
print(chr(97))  # Output: 'a' (Character with ASCII 97)

#-------------------------------5. Data Structure Functions
# a). sorted() – Sort a List
numbers = [4, 2, 9, 1]
print(sorted(numbers))  # Output: [1, 2, 4, 9]
print(sorted(numbers, reverse=True))  # Output: [9, 4, 2, 1]

# b). enumerate() – Get Index and Value While Iterating
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# c). zip() – Combine Two Iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

combined = list(zip(names, ages))
print(combined)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

#---------------------------------6. Functional Programming Functions
# a). map() – Apply a Function to Each Element
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# b). filter() – Filter Elements Based on Condition
numbers = [10, 20, 30, 15, 25]
greater_than_20 = list(filter(lambda x: x > 20, numbers))
print(greater_than_20)  # Output: [30, 25]

# c). reduce() – Reduce an Iterable to a Single Value
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

#---------------------------7. File Handling Functions
# a). open() – Open a File
file = open("demo.txt", "r")
print(file.read())  # Read file content
file.close()

# b). write() – Write to a File
file = open("demo.txt", "w")
file.write("Hello, World!")
file.close()

#-------------------------------8. Miscellaneous Functions
# a). type() – Get Type of a Variable
print(type(10))  # Output: <class 'int'>
print(type("hello"))  # Output: <class 'str'>
print(type([1, 2, 3]))  # Output: <class 'list'>

# b). id() – Get Memory Address of an Object
x = 10
print(id(x))  # Unique ID of the variable

# c). eval() – Evaluate a String as Python Code
expression = "10 + 5 * 2"
print(eval(expression))  # Output: 20
