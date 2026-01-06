"""
Basic Input and Output in Python

This program demonstrates how Python displays output
using the print() function and how different types of
data can be printed to the console.
"""

# Printing simple text output
print("Nihal Mishra")
print("I am learning Python.", "It's fun!")

# Printing multiple statements
print("This is a high level language.")
print("I love coding!")

# Printing numeric expressions
print(5 + 3)    # Addition
print(10 - 2)   # Subtraction
print(4 * 2)    # Multiplication
print(16 / 4)   # Division
print(7 % 3)    # Modulus

# Comments demonstration

# This is a single-line comment

"""
This is a multi-line comment (docstring).
It is used for documentation and explaining
larger sections of code.
"""

# Input in Python 
name = input("Enter your name: ") 
print ("Welcome", name)

age = input("Enter your age: ") 
print ("You are", age, "years old.")

val = input("Enter a number: ")
print (type(val),val) # By default, input() returns a string

val_int = int(val)  # Converting string input to integer
print (type(val_int),val_int)


Name = input("Enter Name :")
age = int(input("Enter Age :"))
marks = float(input("Enter Marks :"))   

print("Name :", Name)
print("Age :", age)
print("Marks :", marks)
