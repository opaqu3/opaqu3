import time
import math
                                          #Operations functions(Add, subtract, multiply, divide)
def add(x, y):
    return x+y

def sub(x, y):
    return x-y 
    

def multiply(x, y):
    return x*y 
    

def divide(x, y):
    return x/y 

def power(x, y):
    return x**y 

def square(num):  
    return num**2 

def sqrt(num):
    from math import sqrt
    return sqrt(num)

def pyth(s1, s2):
    from math import sqrt
    return sqrt(s1 * s1 + s2 *s2)              
    
# floor divison ex, x//y
                                            #UI
print("Hello!")
print("Choose an operation.")

time.sleep(1)
print("1. Add")
time.sleep(1)
print("2. Subtract")
time.sleep(1)
print("3. Mutiply")
time.sleep(1)
print("4. Divide")
time.sleep
print("5. Exponent")
time.sleep
print("6. Square")
time.sleep
print("7. Square Root")
time.sleep
print("8. Pythagorian Theorem")
                                             #Choices for opertions
choice = input("Enter choice(1/2/3/4/5/6/7/8): ")
                                             #if statement for operations
if choice == '1':
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x, "+", y, "=", add(x, y))

    
if choice == '2':
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x, "-", y, "=", sub(x, y))

if choice == '3':
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x, "x", y, "=", multiply(x, y))    

if choice == '4':
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x, "/", y, "=", divide(x, y))    

if choice == '5':
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x, "^", y, "=", power(x, y))

if choice == '6':
    num = int(input("Enter first number: "))
    print(num, "^", 2, "=", square(num)) 

if choice == '7':
    num = float(input("Enter first number: "))
    print("√", num, "=", sqrt(num)) 

if choice == '8':
    s1 = float(input("Enter first side: "))
    s2 = float(input("Enter second side: "))
    print("The third side = ", pyth(s1, s2)) 


time.sleep(50)
print("Your welcome!")




    

