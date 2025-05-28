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


extra_toppings = input("Do you want extra toppings? ")
if 'mushrooms' in extra_toppings:
    print("Adding mushrooms to your pizza.")
elif 'extra cheese' in extra_toppings:
    print("Adding extra cheese to your pizza.")
elif 'pepperoni' in extra_toppings:
    print("Adding pepperoni to your pizza.")
else:
    print("Sorry,we don't serve this topping.")