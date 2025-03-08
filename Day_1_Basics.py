#################### Variables and Naming Conventions ###############################
# Variables store data in memory.
# In Python, you don’t need to declare a variable type explicitly.

z1=23           #int
z2='Ankit'      #string
z3=34.3         #float
z4= True        #boolen

'''Python Data Types (Detailed)
Python has several built-in data types, categorized as:
1️⃣ Numeric types → int, float, complex
2️⃣ Boolean type → bool
3️⃣ String type → str
4️⃣ Sequence types → list, tuple, range
5️⃣ Set types → set, frozenset
6️⃣ Mapping type → dict
7️⃣ Binary types → bytes, bytearray, memoryview'''

####################### Numbers in Python ###############################
a01 = 10         # int  Integer: Whole numbers, positive or negative.No decimal places.
b01 = 3.14       # float: Numbers with decimals. Used in scientific calculations.
c01 = 2 + 3j     # complex: Numbers with real and imaginary parts.Imaginary part is represented by j.
print(c01.real)   #2 output
print(c01.imag)     #3 output

# Numbers operations
x = 10
y = 3

print(x + y)   # 13 (Addition)
print(x - y)   # 7  (Subtraction)
print(x * y)   # 30 (Multiplication)
print(x / y)   # 3.3333 (Division)
print(x // y)  # 3 (Floor Division)
print(x ** y)  # 1000 (Exponentiation)
print(x % y)   # 1 (Modulus)

######################## Strings in Python ##########################
# A sequence of characters enclosed in single (' '), double (" "), or triple quotes (''' ''' / """ """)
# String Creation
s1 = "Hello"
s2 = 'Python'
s3 = """This is a 
multiline string"""
print("The Life Lession by Ankit. \n 1) Don't expect with anyone \n 2) Become knowledgeable with wealthy life \n 3) Respect Our parents and will complete or fulfill their Dreams.")


#String Operations
print("Hello" + "World")  # Concatenation
print("Python" * 3)  # Repeating
print(len(s1))  # Length of string

# String Indexing & Slicing
text = "Python"
print(text[0])   # 'P' (First character)
print(text[-1])  # 'n' (Last character)
print(text[1:4]) # 'yth' (Substring)
print(text[:3])  # 'Pyt' (First 3 chars)
print(text[3:])  # 'hon' (All after index 3)
print(text[0:6:2])
print(text[::-1])   # reverse the string

print(text[::2])   # Every second character
print(text[::-1])  # Reverse the string

# String Concatenation (Joining Strings)
# 1.Using + Operator
a9="Ankit"
b9="Vrema"
c=a9+""+b9
print(c)

# 2. Using join() (Efficient for Large Strings)
a10=["aaaa","jjjjj","kkkkk"]
setup=" ".join(a10)
print(setup)

#String Formatting – Inserting Values into Strings
# 1. Using format()
_a="Raam Raam"
_b="JAI SHREE RAM"
fill="In Every morning start your day by say {} and also say {}".format(_a,_b)

# 2. using f-string -> BEST AND RECOMMENDED
fill1=f"Balo bahiyaa {_a} or bhajman {_b}"
print(fill1)

# String Methods
s = "hello world"

print(s.upper())   # "HELLO WORLD"
print(s.lower())   # "hello world"
print(s.title())   # "Hello World"
print(s.capitalize()) # "Hello World"
print(s.replace("hello", "hi"))  # "hi world"
print(s.split())   # ['hello', 'world']
print(s.find("w"))  # Finds the index of a substring
print(s.count("l"))   # Counts occurrences of a substring

# Counts occurrences of a substring
# 1. Checking If a String Starts/Ends With Something
text = "hello world"
print(text.startswith("hello"))  # True
print(text.endswith("world"))    # True

# 2. Checking for Alphanumeric, Digits, or Alphabets
print("Python123".isalnum())  # True (Only letters & numbers)
print("1234".isdigit())       # True (Only numbers)
print("Python".isalpha())     # True (Only letters)




################ Boolean values ##############
# Represents True or False values. Used in logic-based operations.
print(type(True))
print(10>3)
print(329==23)

#################### TYPE CONVERSION (Type Casting)####################
# Convert data from one type to another.

#1. Implicit Type Conversion (Python automatically converts lower data types to higher ones.)
num = 5
result = num + 2.5  # int + float → float
print(result)  # 7.5
print(type(result))  # Output: <class 'float'>

#2. Explicit Type Conversion Convert types manually using int(), float(), str(), bool().
# Converting string to integer
x = int("100")  # 100 (String to int)

# Converting float to integer
y = int(3.75)   # 3 (Decimal truncated)

# Converting integer to string
z = str(123)    # "123"

# Converting to Boolean
print(bool(0))  # False
print(bool(1))  # True
print(bool("")) # False (Empty string)
print(bool("Python")) # True (Non-empty string)


print(100)
print("HI how are you?")

# 1st method multiple line print

print('''hi,
i can do everything. 
i dont't need anyone help.''')

####################

d = eval(input("Enter whatever : ")) #it performs mathematical operations
print(d)


####################SWAPPING OF TWO VARIABLE####################
'''e5=25
e6=16

e5,e6=e6,e5
print("e5=",e5,"e6=",e6)'''