
#Exercise4-10
list = ['Irham', 'Soikot', 'Sakib', 'Shanto', 'Rasel', 'Naimul', 'Sabbir', 'Shamim', 'Shuvo', 'Sohan']
print("My friends who live out of my city:")
print(list[0:3])
print("My friends who live in my city:")
print(list[4:7])
print("The last 3 index:")
print(list[-3:])

#Exercise4-11
my_pizza = ['cheese', 'pepperoni', 'mushrooms', 'onions']
friend_pizza = my_pizza[:]
my_pizza.append('pineapple')
friend_pizza.append('green peppers')
print("My favorite pizzas are:")
for pizza in my_pizza:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)