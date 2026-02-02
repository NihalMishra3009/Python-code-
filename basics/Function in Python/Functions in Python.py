# Build in Functions
print("Hello World")
var = 1000
print(var)
print(10, 20, 30)

import random
print(random.randint(10, 20))


# user_define functions
# creating Functions
def greeting_someone(name):
    print(f"hello {name} Good morning")
    print(f"{name} Its a beautiful day")

greeting_someone("Nihal")
greeting_someone("Shreya")
greeting_someone("Sujal")


# Examples of User Define Function with passing argument
def even_num(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_num(5)
even_num(6)
even_num(7)


def addition(num1, num2):
    Add = num1 + num2
    print("addition :", Add)

addition(5, 6)
addition(8, 7)


# Return a value or multiple value in function
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = even_odd(10)
print(result)


def number(num1, num2):
    return num1 + num2

val_1 = int(input("Enter a number: "))
val_2 = int(input("Enter a number: "))

val = number(val_1, val_2)
print(val)


# types of argument
# positional argument
def add(a, b):
    return a + b

result = add(5, 6)
print(result)


# Default Argument
def add(a, b, c=0):
    return a + b + c

print(add(5, 6))


# keyword argument or named argument
def add(a, b, c):
    print(f"a:{a},b:{b},c:{c}")
    return a + b + c

add(10, 20, 30)


# Varibale length and positioning argument
# variable length argument
def add(*num):
    return sum(num)

result = add()
print(result)


def studend_details(sid, name, age, *marks):
    percent = sum(marks) / len(marks)
    print(f"{name} with id {sid} secured :{percent}%")

studend_details(101, "john", 19, 79.0, 86.0, 99)
studend_details(102, "john", 19, 59.0, 56.0, 99)
studend_details(103, "john", 19, 49.0, 86.0, 99)
studend_details(104, "john", 19, 66.0, 86.0, 99)


# variable length keyword argument
def student_details(sid, sname, **marks):
    if len(marks) == 0:
        print(f"{sname} did not attempt the exam")
    else:
        percent = sum(marks.values()) / len(marks)
        print(f"{sname} with id {sid} secured {percent}%")

student_details(101, "Nihal", sub1=88, sub2=77, sub3=66, sub4=55)
student_details(102, "NIHAL", sub1=88, sub2=77, sub3=66, sub4=55)
student_details(103, "nihal", sub1=88, sub2=77, sub3=66, sub4=55)


# Doc string in Python function
def div(num1, num2):
    """
    num1: A number to be divided(numerator)
    num2: A number to be divided(denominator)
    :return: float
    """
    if num2 == 0:
        return "Cannot divide as denominator is 0"
    else:
        return num1 / num2

print(div(2, 4))


# passing function in another function (passing function as an arguement)
def add_1(number):
    return number + 1

def square(number):
    return number ** 2

num = int(input("Enter a number: "))
res = square(add_1(num))
print(f"Output is :{res}")
