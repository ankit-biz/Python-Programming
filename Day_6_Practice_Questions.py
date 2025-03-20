# Q1. Write a Python program that takes an integer input from the user and prints whether it is positive, negative, or zero.
'''take=int(input("Enter any no."))

if take<0:
    print(f"{take} this is negative number")

elif take==0:
    print(f"you entered {take}")

elif take>=1:
    print(f"{take} this is positive number")

else:
    print("Enter valid number")'''

# Q2. Create a program to find the largest of three numbers using nested if statements.
'''a, b, c= map(int,input("Enter three numbers").split())
if a>b:
    if a>c:
        print(f"{a}")
    else:
        print(f"{c}")
else:
    if b>c:
        print(f"{b}")
    else:
        print(f"{c}")'''

# Q3. Implement a program that takes input for age and checks if the person is eligible to vote (18+).
'''age=int(input("Enter your age:- "))
if age>=18:
    print(f"as per your age {age}, You can vote.")
else:
    print(f"sorry! you are not eligible because your age is {age}, that is less than 18")
'''
# Q4. Check if a number is even or odd.
'''a=343
if a%2==0:
    print("Even")
else:
    print("Odd")'''

# Q5. Assign grades based on marks-> A (90-100), B (80-89), C (70-79), F (<70).
'''marks=81
if marks>=90 and marks<=100:
    print("you got grade \"A\" ")
elif marks>=80 and marks<=89:
    print("you got grade \"B\" ")
elif marks>=70 and marks<=79:
    print("you got grade \"C\" ")
elif marks<=70:
    print("you got grade \"F\" ")
else:
    print("Enter Valid")'''

# Q6. Check if a year is a leap year.
'''year=2024
if year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")'''

# Q7. Build a calculator that takes two numbers and an operator (+, -, *, /).
'''symbol=input("Enter arithemetic symbol with that you want operations:-")
number1, number2= map(int, input().split())
if symbol=='+':
    result=number1+number2
    print(f"{number1} + {number2} = ",result)
elif symbol=='-':
    result=number1-number2
    print(f"{number1} - {number2} = ",result)
elif symbol=='*':
    result=number1*number2
    print(f"{number1} * {number2} = ",result)
elif symbol=='/':
    result=number1/number2
    print(f"{number1} / {number2} = ",result)
else:
    print("Choose the arithmetic operator in that \"+,-,*,/\"")
'''
# Q8. Print numbers from 1 to 100 using a for loop.
'''for i in range(1,101):
    print(i,end="--")'''

# Q9. Print the multiplication table of a given number using a while loop.
'''table=int(input("Enter the number that you want table"))
counter=1
while counter<=10:
    result= table * counter
    print(f"{table} * {counter} =",result)
    counter +=1'''

# Q10. Use a for loop with else to check if a number is prime.
'''num = int(input("Enter a number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
print("Prime" if is_prime else "Not prime")'''

# Q11. Calculate the sum of all numbers from 1 to n.
'''enter=4
total=0
for i in range(1,enter+1):
    total +=i
    print(f"{total}")'''

# Q12. Compute the factorial of a number using a loop.
'''enter=5
factorial=1
for i in range(1,enter+1):
    factorial *=i
    print(f"{i}:{factorial}")'''

# Q13. Print the Fibonacci sequence up to n terms.
'''
n = int(input("Enter the number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b'''

# Q14. Print the pattern
'''for i in range(1,10):
    print("*" *i)'''

# Q15. Count the number of vowels (a, e, i, o, u) in a string.
I=input("Enter words").lower()
vowels="aeiou"
count=0
for i in I:
    if i in vowels:
        count +=1
print(count)

# ------------------------------------------ Practice----function
#Write a function that takes two numbers and returns their sum.
def sum(a,b):
    formula=a+b
    return formula
print(sum(64,5))

#2️Create a function that takes a string and returns its reverse.
def re(a):
    asa=a[::-1]
    return asa
print(re("Ankit"))

#3️Write a function that checks whether a given number is even or odd.
def check(a):
    if a%2==0:
        print(f"{a} is a even number")
    else:
        f"{a} is a odd number"
check(4634364)

#4️Create a function that takes a list and returns the largest element.
lis=[32,432,64,243,643,75]
def largest():
    ck=max(lis)
    print(ck)
largest()

#5️Write a function that takes two numbers and returns the greater #on
def two(number1, number2):
    if number1>number2:
        return f"{number1} is greater than {number2}"
    else:
        return f"{number2} is greater than {number1}"

print(two(43,4))

#6 Write a function that accepts a name and age as arguments and prints a greeting message.
def message(name, age):
    return f"Hi {name} welcome to our team, and according to your age {age}, you touched the success"

print(message("anmkit",21))

#7 Create a function that returns multiple values (sum, difference, product, and quotient) of two numbers.
def calc(a,b):
    sum=a+b
    difference=a-b
    product=a*b
    quotient=a/b
    yield  sum,difference,product,quotient
a=calc(13,345)
print(a)

#8 Write a function that takes a list and returns a tuple containing the sum and average of the list elements.
list1=[123,42,564,6,78]
def take(list1):
    su=sum(list1)
    avg=sum(list1)/len(list1)
    return su,avg
print(take(list1))

#9 Implement a function that takes default arguments and returns a greeting message.
def defu(name="Nagar"):
    return f"Hi {name}, nice to meet you"

print(defu())

#🔟 Create a function that accepts *args and returns the sum of all numbers passed to it.
def took(*args):
    return sum(args)
print(took(432,35,65,86))
