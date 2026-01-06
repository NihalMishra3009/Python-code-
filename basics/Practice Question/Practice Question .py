# Question : write a program to input 2 number & print their sum, difference, product & quotient.
num1 = int(input("Enter First number : "))
num2 = int(input("Enter Second number : ")) 
sum = num1 + num2 
diff = num1 - num2
prod = num1 * num2
quot = num1 / num2

print("sum of two number is :", sum)
print("difference of two number is :", diff)
print("product of two number is :", prod)
print("quotient of two number is :", quot)


# WAP to input side of square And print its area & perimeter.
side = float(input("Enter sides of square :  "))
area = side* side 
perimeter = 4 * side 

print ("Area of Square : ", area)
print("Perimeter of Square : ", perimeter)

# WAP to input 2 floating point number & print their average 
num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))

average = (num1 + num2) / 2

print("Average of two number is : ", average)

# WAP to input 2 int number , a and b.Print true if a is greater than or equal to b , otherwise print false.
a = int(input("Ennter The First Number :"))
b = int(input("Enter The Second Number :"))

print ("if a is greater than or equal to b : ", a >= b)
