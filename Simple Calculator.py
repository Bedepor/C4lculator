"""
Filename: simple_calculator.py
Author: <Claros, Firstname>
Created: <08/27/2025>
Instructor: Holtslander
"""
print("Hello This is simple Calculator this program takes the users inputs and does 4 simple operations")
num1 = input("Please input your first number without any commas.\n")
num2 = input("Please input your second number without any commas.\n")

num1 = int(num1)
num2 = int(num2)

print(f"{num1} + {num2} = {num1 + num2} ")
print(f"{num1} - {num2} = {num1 - num2} ")
print(f"{num1} * {num2} = {num1 * num2} ")
print(f"{num1} / {num2} = {num1 / num2} ")
print("thank you for using simple calculator!")