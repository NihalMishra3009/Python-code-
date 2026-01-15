# List in Python (Module 6)

name = "John"
age = 20
percentage = 86.5

student = ["John", 20, 86.5]
print(student)
print(type(student))

day_of_week = ["monday", "tuesday", "wednesday", "thursday",
               "friday", "saturday", "sunday"]

print(day_of_week[3])
print(day_of_week[4])

# Negative indexing in list
print(day_of_week[-1])
print(day_of_week[-3])

# Length of list
print(len(day_of_week))
print(f"last day of the week is {day_of_week[-1]}")

# -----------------------------
# List Operations

# Slicing of list
l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(l1[1:8:2])

# Concatenation in list
l2 = [0, 5]
print(l1 + l2)
print(l2 + l1)

# Repetition of list
print(l2 * 4)

# -----------------------------
# List Functions

# append()
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# insert()
fruits.insert(2, "Dragon fruit")
print(fruits)

# extend()
fruits.extend(["Grapes", "Mango"])
print(fruits)

# remove()
fruits.remove("banana")
print(fruits)

# pop()
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)

# -----------------------------
# reverse(), sort(), count()

day_of_week.reverse()
print(day_of_week)

num = [4, 9, 0, 1, 2, 8]
num.sort()
print("Sorted list:", num)

num.reverse()
print("Reverse sorted list:", num)

num1 = [0, 1, 3, 4, 1, 0, 0, 3, 0]
print("Original list:", num1)

COUNT = int(input("Enter the number to calculate count in that list: "))
print("Occurrence of", COUNT, "in the list:", num1.count(COUNT))

# -----------------------------
# Membership operator

language = ["Java", "C++", "Python"]
print("Python" in language)
print("C++" not in language)

# -----------------------------
# Numerical operations

l3 = [1, -2, 3, 4, 5, 26]
print("Smallest Number:", min(l3))
print("Largest Number:", max(l3))
print("Sum:", sum(l3))

# -----------------------------
# Nested list

l4 = [5, 1.5, "Python", True, None, [1, 2, 3], 10]
print(len(l4))
print(l4[-2])
print(l4[-2][0])

l5 = [[1, 2], [3, 4], [5, 6, [0, 1]]]
print(l5[-1][-1][1])
