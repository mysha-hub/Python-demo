requested_toppings = ['peparoni', 'extra cheese', 'mashrom']
for requested_topping in requested_toppings:
    print(f'We are putting{requested_topping} in our pizza.')
print("\nWe are done making pizza.")

requested_toppings = ['mushroom', 'green onion', 'shrimp']
for requested_topping in requested_toppings:
    print(f'My favorite topping is {requested_topping}. ')
print("\nThis are my favorite toppings.")


requested_topping = ['green onion', 'cheese', 'ham', 'beef becon']
for requested_topping in requested_toppings:
    if requested_topping == "green onion":
        print("sorry, we are run out of this topping.")
    else:
        print("sir,please wait.")
