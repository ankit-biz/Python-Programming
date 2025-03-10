####################OPERATORS & OPERANDS####################
'''An operator is a symbol that performs an operation on operands (variables, values).
Operators in Python can perform various operations like arithmetic, comparison, logical, bitwise, etc.
Examples of operators:

Arithmetic: +, -, *, /, %
Comparison: ==, !=, <, >, <=, >=
Logical: and, or, not
Bitwise: &, |, ^, ~
'''

#------------------------1.Arithmetic Operation---------------------------
# These operators perform mathematical operations like addition, subtraction, multiplication, etc.
a, b = 10, 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333   Returns quotient (floating-point)
print(a // b)  # 3          Returns quotient (integer)
print(a % b)   # 1          Returns remainder
print(a ** b)  # 1000 (10^3)    Raises to the power


#------------------------------2.COMPARISION OPERATORS-----------------------------------

# {'<' less than}, {'==' Equal to}, {'<='less than or equalto}, {'>=' Greater than or equalto}, {'!=' not equalto} it always return Boolean value
'''print(3<1)
print(12==12)
print(13<=44)
print(1223>=2323)
print(22!=22)
'''
#--------------------------------3.LOGICAL OPERATORS---------------------------------------

# {'AND' if the both statement are true then it give 'TRUE' other wise false},it {perform logical operations and return a Boolean value}
# {'OR' if the both statement or only one statement is true it give 'true'}
# {'NOT' if the statement is true it convert into false and vice versa}

'''c=22<10 and 65>8
c1=52>=765 or 28645<=978
c2=not(2<10 and 65>8)
print(c)
print(c1)
print(c2)
'''
#---------------------------------4.ASSIGNMENT OPERATORS-----------------------------------
# Used to assign values to variables.
#Assignment operator are used to assign the value to the  variable, Types are "=", "+=", "-=", "*="
'''Assign	'='	a = 10	a = 10
Add & Assign	'+='	a += 5	a = a + 5
Subtract & Assign	'-='	a -= 3	a = a - 3
Multiply & Assign	'*='	a *= 2	a = a * 2
Divide & Assign	'/='	a /= 2	a = a / 2'''

#---------------------------------5.IDENTITY and MEMBERSHIP OPERATORS-------------------------------------

#Identity operators check if two operands refer to the same object in memory. Types are  "is" & "is not"
#These check if a value is present in a sequence (list, tuple, set, dictionary).

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True (same object)
print(x is not z)  # True (different objects)
print(2 in x)      # True
print(5 not in x)  # True


#---------------------------------6.BITWISE OPERATORS------------------------------

#Bitwise operator are use to compare the binary(0=on, 1=off) numbers. Types
#AND(&)
#OR(|)
#XOR(^)
#<<,>>
'''e1=15
e2=8

print(e1 & e2)
print(e1 | e2)
print(e1 ^ e2)
print(bin(10)) #it is used to find out the binary code'''


##################################################################################
#--------------------------CONDITIONAL STATATEMENTS-------------------------------
##################################################################################

#Conditional statements allow computer to execute a certain condition only if it is true. Types "if", "if-else", "if-elif-else", "Nested statement",

#-------------------------1. if statement-------------------
# Executes a block of code only if the condition is True.
'''e3=27
if e3<=27:
    print("You are genius")

print("Bluddy fool")'''
#Short hand if statement :is used for fast execution and it is onle liner
'''e7=9
if e7>=90: print("Welcome genius")'''

#-------------------------2.if-else statement-------------------
# Executes one block if the condition is True, otherwise another block executes.

'''print("Let's check you matuarity")

e4=int(input("Enter your age "))

if e4>=18:
    print("YOU are Mature and Just ask the same question with yourself. 🤣")
else:
    print("You are not mature")

print("Thank u")

#Short hand if statement :is used for fast execution and it is onle liner
e4=19
print("YOU are the winner and you got a car")  if e4>=18 else print("You are not mature")'''

#--------------------------3.if-elif-else statement------------------------
# Used when there are multiple conditions to check.

'''e5 = int(input("Enter your age "))

if e5>= 18:
    print("Congrats!")
elif e5>12:
    print("You are a baby")
else :
    print("You need to feed your mother milk")'''

'''x = 10

if x >= 550:
    print("you get A grade")
elif x >=450:
    print("you get B grade")
elif x >= 300:
    print("you get C grade")
else:
    print("You Just Pass, Keep it Up and levelup")'''

#------------------------------4.Nested if statements-------------------------------
'''e6=int(input("Enter your marks"))

if e6>=90:
    print("you got a MacBook")
    if e6>=95:
        print("You got a I Phone 10")
        if e6>=98:
            print("You got a Drone")
elif e6<85:
    print("You need to do some effort")
else:
    print("you are not alligible for this concert")
'''
'''num = 15

if num > 10:
    print("Number is greater than 10")
    if num % 2 == 0:
        print("It is even")
    else:
        print("It is odd")

'''

'''Questions Practice'''
#Write a program to  check the  number is even or odd
'''f=int(input("Enter the number to check the number is even or odd"))

if f%2==0:
    print("Number is even")
elif f%3==1:
    print("Number is odd")
else:
    print("Please enter correct number")
'''
##Write a program for area calculator

'''print("*********Basics area Calculator*********")
print("Enter 1 for Circle")
print("Enter 2 for Square")
print("Enter 3 for Triangle")
print("Enter 4 for Rectangle")

f1=int(input("Enter the The number which area you want to find"))
if f1==1:
    f2=float(input("Enter the radius"))
    area=22/7*(f2**2)
    print("Area of the  circle is", area)

elif f1==2:
    f2 = float(input("Enter the Side"))
    area = f2 ** 2
    print("Area of the Square is", area)

elif f1==3:
    f2 = float(input("Enter the Base: "))
    f3 = float(input("Enter the Height: "))
    area = 1/2*(f2*f3)
    print("Area of the Square is", area)

elif f1==4:
    f2 = float(input("Enter the length: "))
    f3 = float(input("Enter the bregth: "))
    area = f3 * f2
    print("Area of the rectangle is", area)

else:
    print("Enter the valid number between 1-4")'''

## Write a program to check in the letters vowels are presented or not

'''g=input("Enter the letter")
if  (g in "aeiou") or (g in "AEIOU"):
    print("It's a vowel")
else:
    print("it's not a vowel")'''

## Wite a program to find out the number's digit
'''h=int(input("Enter the  number: "))

if h>=0 and h<=9:
    print("Number is one digit")

elif h>=10 and h<=99:
    print("Number is ten's digit")
else:
    print("Google it")'''