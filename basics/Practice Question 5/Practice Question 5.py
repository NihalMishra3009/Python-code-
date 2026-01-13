"""
WAP for compound Interest
amount = p (1+ r/100)** t
ci = amount - p
"""

principle = float(input("Enter the principle amount:"))
rate = float(input("Enter the interest rate:"))
time = float(input("Enter the time:"))
amount = principle *(1 + rate/100) ** time
ci = amount - principle
print("amount:",round(amount,2))
print("ci:",round(ci))

