age = int(input("Enter your age:"))
if age < 4:
    price = 0
elif age < 10:
    price = 15
elif age < 18:
    price = 20
else:
    price = 35
print(f"Your ticket price is ${price}.")
# This code determines the ticket price based on the age of the person.
# It uses an if-elif-else statement to check the age and assign the appropriate price.