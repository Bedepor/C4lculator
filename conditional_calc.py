# num = input("Type a number\n")
#num = int(num)
#if num % 2 == 0:
#    print(f"{num},is an even number")
#elif num % 5 == 0:
#    print(f"{num},is divisble by 5")
#else:
#    print(f"{num},is an odd number")
#print ("done")
"""
Filename: simple_calculator.py
Author: <Claros, Firstname>
Created: <08/27/2025>
Instructor: Holtslander
"""
print("Hello This is simple Calculator this program takes the users inputs and does the operations")
num1 = input("Please input your first number without any commas.\n")
op = input("Please input your operator\n"
            "for addition enter: +\n"
            "for subtraction enter: -\n"
            "for multiplication enter: *\n"
            "for division enter: /\n")
num2 = input("Please input your second number without any commas.\n")

num1 = int(num1)
num2 = int(num2)

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
print("thank you for using simple calculator!")