car = ['toyota', 'honda', 'ford', 'chevrolet', 'nissan', 'bmw', 'subaru', 'volkswagen', 'hyundai', 'kia']
a = input("Sir,which car do you want to buy?")
if a in car:
    print(f"Ok sir, let me bring {a} for you.")
else:
    print(f"Sorry sir , we don't have {a} in our stock.")
# This code checks if the user's input car is in the predefined list of cars.
