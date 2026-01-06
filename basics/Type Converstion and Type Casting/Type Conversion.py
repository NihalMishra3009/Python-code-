# -------------------------------
# Type Conversion (Automatic)
# -------------------------------

a = 2        # integer
b = 3.5      # float

# Python automatically converts int to float
# so that addition is possible
print(a + b)        # Output: 5.5
print(type(a + b)) # <class 'float'>


# -------------------------------
# Type Casting (Manual)
# -------------------------------

x = 5

# Converting integer to float
x_float = float(x)
print(x_float)           # 5.0
print(type(x_float))     # <class 'float'>

# Converting integer to string
x_str = str(x)
print(x_str)             # '5'
print(type(x_str))       # <class 'str'>


# -------------------------------
# Type Casting with User Input
# -------------------------------

# input() always returns string
num1 = input("Enter a number: ")
print(type(num1))        # <class 'str'>

# Convert string to integer
num1_int = int(num1)
print(num1_int + 10)     # Performs numeric addition


# -------------------------------
# Common Real-Life Example
# -------------------------------

price = "99.50"          # price coming as string

# Convert string to float for calculation
price_float = float(price)
print(price_float + 10)  # 109.5
