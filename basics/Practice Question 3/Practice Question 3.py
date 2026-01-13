# WAP To calculate AREA of Traingle

"""When All the length of the sides of the triangle is known -a,b,c
semi perimeter (s) = (a + b + c)/2

Area = square root of (s*(s-a)*(s-b)+(s-c))"""

a= float(input ("Enter First side of Traingle "))
b= float(input ("Enter First side of Traingle "))
c= float(input ("Enter First side of Traingle "))

s = (a*b*c)/2
area =  (s*(s-a)*(s-b)+(s-c) ** 0.5)

print ("area of Traingle",round(area,2))

print("Perimeter of Traingle ",s)


# WAP TO calculate Right angle Traingle
# Given base
# height

Base = float(input("Enter Base of Traingle "))
Height = float(input("Enter Height of Traingle "))

area = (Base*Height)/2

print("Area of Right Traingle",round(area,2))

