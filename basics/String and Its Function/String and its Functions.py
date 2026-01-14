# =====================================================
# STRINGS AND STRING FUNCTIONS IN PYTHON
# =====================================================

# -----------------------------
# 1. Types of Strings
# -----------------------------

# Single quote string
str1 = 'This is a string'

# Double quote string
str2 = "This is also a string"

# Triple quote string (used for multi-line strings)
str3 = """This is
a multi-line
string"""

print(str1)
print(str2)
print(str3)

# -----------------------------
# 2. Escape Sequence Characters
# -----------------------------

# \n → new line
str4 = "This is my string.\nWe are creating it in Python."
print(str4)

# \t → tab space
str5 = "This is my string.\tWe are creating it in Python."
print(str5)

# \\ → backslash
print("new\\old")

# \' → single quote inside single-quoted string
print('This is Python\'s class')

# -----------------------------
# 3. Basic String Operations
# -----------------------------

# String length
s1 = "Hello"
print(len(s1))  # Length of string

# String concatenation
s2 = "Nihal"
final_str = s1 + " " + s2
print(final_str)
print("Total length:", len(final_str))

# -----------------------------
# 4. Indexing in Strings
# -----------------------------

text = "PythonProgramming"

# Positive indexing
print(text[3])      # Character at index 3
print(text[0])      # First character

# Negative indexing
print(text[-1])     # Last character
print(text[-4])     # 4th character from end

# -----------------------------
# 5. Slicing in Strings
# -----------------------------

word = "HelloWorld"

print(word[1:5])     # From index 1 to 4
print(word[:5])      # From start to index 4
print(word[5:])      # From index 5 to end
print(word[2:9:2])   # With step value

# Negative slicing
print(text[-7:-1])

# -----------------------------
# 6. String Functions
# -----------------------------

sentence = "i am studying python programming language"

# endswith()
print(sentence.endswith("age"))
print(sentence.endswith("xyz"))

# capitalize()
print(sentence.capitalize())

# replace()
s10 = "I love Python. Python is great."
print(s10.replace("Python", "Java"))

# find()
print(s10.find("Python"))   # Returns index
print(s10.find("Java"))     # Returns -1 if not found

# count()
print(s10.count("Python"))
print(s10.count("t"))

# -----------------------------
# 7. Case Conversion Functions
# -----------------------------

s3 = "Python"

print(s3.upper())       # Uppercase
print(s3.lower())       # Lowercase
print(sentence.title()) # Title case
print(sentence.capitalize())

# -----------------------------
# 8. startswith() and endswith()
# -----------------------------

s4 = "We are learning Python. Python is fun"

print(s4.startswith("We"))
print(s4.startswith("we"))
print(s4.endswith("fun"))
print(s4.endswith("Fun"))

# -----------------------------
# 9. String Formatting
# -----------------------------

name = "John"
age = 20
language = "Python"
hours = 3

# Normal print
print(name, "is", age, "years old. He studies", language, hours, "hours a day")

# f-string (recommended)
print(f"{name} is {age} years old. He studies {language} {hours} hours a day")

# -----------------------------
# 10. Arithmetic inside f-strings
# -----------------------------

sub1 = 78
sub2 = 87
sub3 = 91

total = sub1 + sub2 + sub3
percentage = total / 3

print(f"{name} scored {total} marks in the test")
print(f"{name} scored {round(percentage, 2)}% in the test")

# -----------------------------
# 11. Counting Substring Occurrences
# -----------------------------

main_str = "We are learning Python. Python is fun"
sub_str = "Python"

print(f"Occurrence of '{sub_str}' is {main_str.count(sub_str)}")
