#Today we are going to learn Different types of operators in Python

# Arithmetic Operators
a = 10
b = 7

print(a+b)  # Addition
print(a-b)  # Subtraction
print(a*b)  # Multiplication
print(a/b)  # Division
print(a%b)  # Modulus                               """To get the remainder"""
print(a**b) # Exponentiation                        """To get the power""" a^b

#Relational Operators
a = 50
b = 20 

print (a == b) #false              
print (a != b) #true                    
print (a >= b) #true  
print (a > b) #true                  
print (a <= b) #false  
print (a < b) #false        

#Assignment Operators
sum = 10 
sum += 10     # sum = sum + 10
sum -= 5      # sum = sum - 5                       #subtraction equal to
sum *= 2      # sum = sum * 2                       #multiplication equal to
sum /= 5      # sum = sum / 5                       #division equal to
sum %= 3      # sum = sum % 3                        #modulus equal to
print ("sum :", sum)

# Logical Operators

# Not Operator
a= 50 
b= 20
print (not (a > b))  # False
print (not False)  # True
print (not True)   # False

# And operator
num1 = True 
num2 = False
print ("AND operator:", num1 and num2)

# Or operator
a = 20
b = 50
print ("OR operator:", a or b)
print ("OR operator:", (a == b) or (a > b))







