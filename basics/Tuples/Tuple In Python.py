# -------------------------------
# TUPLES IN PYTHON
# -------------------------------
# Tuple = ordered, immutable collection
# Syntax: (item1, item2, item3, ...)

t1 = ("Python", 1.5, 1, True, None, [1, 2, 3], (10, 20))

print("Tuple:", t1)
print("Type of t1:", type(t1))
print("Length of t1:", len(t1))

# Accessing elements using index
print("First element:", t1[0])
print("Last element:", t1[-1])
print("Last element of nested tuple:", t1[-1][-1])

print("\n-------------------------------")

# Tuple without parentheses (packing)
t2 = 10, 20, 30
print("Tuple t2:", t2)
print("Type of t2:", type(t2))

print("\n-------------------------------")

# Converting list to tuple (type casting)
l1 = [1, 2, 3]
t3 = tuple(l1)
print("List to Tuple:", t3)
print("Type:", type(t3))

# Converting tuple to list
t4 = (4, 5, 6)
l2 = list(t4)
print("Tuple to List:", l2)
print("Type:", type(l2))

print("\n-------------------------------")

# -------------------------------
# MUTABILITY vs IMMUTABILITY
# -------------------------------

# List is mutable
list1 = ["hello", "hi", "hey"]
print("Original list:", list1)
print("List ID before change:", id(list1))

list1[-1] = "hey there"
print("Modified list:", list1)
print("List ID after change:", id(list1))  # Same ID

print("\n-------------------------------")

# Tuple is immutable
tuple1 = (1, 2, 3)
print("Tuple:", tuple1)
print("Tuple ID:", id(tuple1))

# tuple1[0] = 100  ❌ This will cause an error (immutable)

print("\n-------------------------------")

# Reference behavior with lists
str1 = ["hello", "hi", "hey"]
str2 = str1  # Both point to same list

str1[-1] = "hey they"

print("str1:", str1)
print("str2:", str2)
