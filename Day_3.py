########################LOOPS (for & while)########################
#loop is to repeat something in the exact same way or Used to iterate over a sequence (list, tuple, string, range). Types

#1. for     (Syntax : for variable in sequence: # Code to execute)

fruuits= ['Apple', 'Banana', 'Cherry', 'Dragon Fruit','Fish']
for fruit in fruuits:
    print(fruuits)

for fruit in fruuits:
    print(fruit)

for i in range(1,10):   # in that end print the output in single line
    print(i,end="")

for i in range(10,1,-1):   # reverse loop
    print(i)

for i in range(1,10):
    print("Hellow world!")

for i in range(1,11,2):     # gaps between the numbers
    print(i)

for i in range(0,5,2):
    print(i)

table=int(input("Enter the number that you want to find the table \n"))         #table

for i in range(1,11):
    print("%d * %d ="%(table,i),i*table)

# Looping Through Different Data Structures
for j in 'Ankit':       #Iterating Over Strings
    print(j)

#Iterating Over a List with Index using enumerate()
fruuits= ['Apple', 'Banana', 'Cherry', 'Dragon Fruit','Fish']
for index, fruit in enumerate(fruuits):
    print(f"INDEX {index}:{fruuits}")

#Iterating Over a Dictionary using .items()
data={"name":"Ankit","qualification":"BCA","sex":"male","age":21}
for key,value in data.items():
    print(f"{key}:{value}")

## For loop with conditional statement
'''for i in range(1,101):
    if i%3==0 and i%2==0:
        print(i)'''

#2. while loop : it execute till the give condition if not true

count=1
while count<=5:
    print(count)
    count += 1
'''a1=int(input("Enter the number"))
while a1<=10:
    print(a1)
    a1 +=1'''

#3. while true: it is an infinite loop, to stop while true loop we used "break statement ".
'''while True:    infinite loop
    print("hello ankit")'''

'''while True:      # table with taking input value and consist of break
    table = int(input("Enter the first value"))

    for i in range(1,11):
        print("%d * %d =" % (table, i), i * table)

    repeat = input("if you want to stop the Enter 'yes': ")
    if repeat=="yes":
        break'''

#4. nested : when loop inside a loop is called as nested loop. it is also used for solve pattern problems.
'''for i in range(1,4):     # outer loop then inner loop
    for j in range(1,10):
        print(j, end="")
    print()'''

'''for i in range(1,10):
    for j in range(1,i+1):
        print(j, end="")
    print()
'''
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()

# Loop Control Statements (break, continue, pass)
###################BREAK & CONTINUE STATEMENT######################
#BREAK: it used when you want to destroy a loop at certain condition and come out of the loop.
'''for i in range(1,10):
    if i==6:
        break
    print(i)'''
#CONTINUE: it used when you want to skip a particular condition.
'''for i in range(1,10):
    if i==3:
        continue
    else:
        print(i)'''
#PASS: The pass statement does nothing and acts as a placeholder.
for i in range(2,3):
    pass ## Placeholder for future code

#write a program to sum all even number from 1 to 20
'''sum=0
for i in range(1,50):
    if i%2==0:
        sum +=i
print("sum of all even numbers 1 to 50 is", sum)'''

#write a program to write first 20 numbers and their square rooths

'''for i  in range(1,21):
    print(i,"=",i*i)'''

#write a program to find the of first 10 odd numbers sum.
'''sum=0
x=0
while x<=20:
    if x%2 !=0:
        sum += x
    x+=1
print(sum)
'''
#write a program if a number is divisible by 8 and 12 up to 100 numbers.
'''for i in range(1,100):
    if i%8==0 and i%12==0:
        print(i)'''

#write  a program to create billing system at supermart

#pattern
'''for i in range(1,7): #row
    for j in range(1,i+1): #colum
       # print(j,end="")
        print(i, end="")
    print()'''

for i in range(1,7): #row
    for j in range(7,i,-1): #colum
        print(i, end="")
    print()
