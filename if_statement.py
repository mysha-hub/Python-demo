cars = ['bmw', 'audi', 'toyota', 'ford']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())



# Check if a requested topping is not anchovies
requested_topping = input("Enter a pizza topping: ")
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
# Check if a requested topping is not anchovies, using an if-else statement