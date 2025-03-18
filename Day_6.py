#########Input and Output Functions##########
#Python provides two essential functions for handling input and output operations:

#print() #→ Used for displaying output.
#input() #→ Used for taking user input.

# 1. The print() Function (Output in Python)

# syntax: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
####*objects: The values to be printed. You can pass multiple objects separated by commas.
####sep: (Optional) Specifies the separator between objects. Default is a space (' ').
####end: (Optional) Specifies what to print at the end. Default is a newline ('\n').
####file: (Optional) Specifies where to write the output. Default is sys.stdout (the console).
####flush: (Optional) If True, the stream is forcibly flushed. Default is False.

#Basic Usage of print()
print("Hello, world!")

# 2. Print Multiple Arguments
a = "Ankit Verma"
b = 21
print("My name is", a, "and I'm", b, "years old.")

# 3. Using sep Parameter (Separator)
print("Hi,", "How can i help you?", "let's start the party",
      sep="$")  # default saperator is "" space. you can change to - , | etc.

# 4. Using end Parameter (Custom Line Ending)
print("Chakal", end=" ")  # By default, print() adds a newline (\n) at the end, but we can change it.
print("Nobody")
print("patthaa", end="....?")

# 5. Printing Special Characters (Escape Sequences)

##########Escape Sequence	    Description	            Example Output
##########\n	                New Line	       "Hello\nWorld" → HelloWorld
##########\t	                Tab Space	        "Hello\tWorld" → Hello World
##########\\	                Backslash	        "C:\\Users\\Ankit" → C:\Users\Ankit
##########\'	                Single Quote	    "I\'m Ankit" → I'm Ankit
##########\"	                Double Quote	    "Hello \"World\"" → Hello "World"

# 6. String Formatting (f-strings, format(), % Operator)
# a). using f-string     -> recconmended in latest tech,f-strings are faster and more readable, so they are preferred.
a1 = "laptop"
b1 = "depression"

print(f"i have spend my most of time with {a1}, due to that i go through in deep this cause me {b1}")

# b). using format
print("i have spend my most of time with {}, due to that i go through in deep this cause me {}".format(a1, b1))

# c). using % Operator (Old method)
print("i have spend my most of time with %s, due to that i go through in deep this cause me %s" % (a1, b1))

# 7. Printing in Different Number Formats
pi = 3.14159265358979

print(f"Rounded Pi: {pi:.2f}")  # 2 decimal places
print(f"Binary of 10: {10:b}")  # Binary format
print(f"Hexadecimal of 255: {255:x}")  # Hex format

with open("reading.txt", "w") as f:
    print("Writing to a file", file=f)


#-----------------------------------------------------------------------------------------------------------------------
###################The input() Function (Taking User Input)################
# The input() function allows users to enter data via the keyboard.
'''enter=input("Enter your name")          # input() always returns a string, even if the user enters a number.
print(f"My name is {enter}")
print(("My name is"),enter)'''

# 1. Converting Input to Numbers
'''ag = int(input("Enter your age: "))        # Convert input to int, float, or bool for numerical operations.
print("In 5 years, you will be", ag + 5)

e1=bool(input("male=0, female=1 "))
if e1==0:
    print("Happy Gourney")
else:
    print("that's great")'''

# 2. Taking Multiple Inputs (split Method)
'''name, age=input("tha").split()          # The space-separated input is split into name and age. print(f"mera naam 
{name} hai. mai {age} saal ka hu, Dhanyawaad")        # enter the values like "lallu 32", both at the same time'''
# 3. Taking List Input (map Function)
# -> If we need multiple numbers, we can use map().
'''ka=list(map(int,input("entre the input separated by space").split()))
print("Numbers:",ka)
'''
#4. Taking Input with a Specific Separator
'''ki = list(map(int, input("Enter numbers separated by commas: ").split(",")))
print("Numbers:", ki)'''


#5. Summary Table
###Function	                    Description	            Example Output
###print(x)	                    Displays output	print   ("Hi") → Hi
###print(a, b, sep="-")	        Custom separator	    "B-C"
###print(a, end=" ")	        Custom line ending	    ello World!
###\n, \t, \\	                Escape sequences	    Hello\nWorld" → Newline
###f"{var}"	                    f-string formatting	    "Value: 10"
###input()	                    Takes user input	    enter name: Ankit"
###int(input())	                Convert input to integer age = int(input())
###map(int, input().split())	Multiple inputs	          [1, 2, 3]

#6. Handling Errors in Input
'''try:
    inl=int(input("let age"))
    print(f"your age is {inl}")
except ValueError:              # valueerror optional
    print("Enter INT data type value")'''
