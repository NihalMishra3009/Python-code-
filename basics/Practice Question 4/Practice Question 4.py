"""
Simple interest = (P * R * T)/100
P = Principle amount
R = rate of interest
T = time duration
"""

principle = float(input("Enter the principle amount:"))
rate = float(input("Enter the interest rate:"))
time = float(input("Enter the time:"))
s1 = (principle*rate*time)/100

print("Simple interest",s1)