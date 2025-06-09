alien_0 = {'color': 'yellow', 'points': 10, 'speed': 'slow'}
alien_1 = {'color': 'green', 'points': 15, 'speed': 'medium'}
my_dict = {}
n = int(input("Enter the number of keys:"))
for i in range(n):
    key = input("Enter the key:")
    value = input("Enter the value:")
    my_dict[key] = value
    print("alien_2:", my_dict)
