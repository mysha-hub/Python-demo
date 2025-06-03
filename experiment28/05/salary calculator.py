a = int(input("How many days do you work per weak? "))
b = int(input("How many hour  maximam do you work per day ? "))
e = float(input("Minimum wage :"))
f = float(input("Maximum wage :"))
g = float(input("Rate of dollar to taka : "))
h = a * b * g * e * 4 #minimum wage
k = a * b * f * g * 4 #maximum wage
print(f"Your salary minimum  is {h} taka per month.")
print(f"Your salary maximum wage is {k} taka per month.")
