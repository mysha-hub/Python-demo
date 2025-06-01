alien_o = {'color':'green', 'points':5}
print(alien_o['color'])
print(alien_o['points']


alien_0 = {'color': 'red', 'food': 'pizza'}
print(f'The alien color is {alien_0['color']}.')
print(f'My favorite food is {alien_0['food']}.')      


alien_0 = {'color': 'yellow', 'food': 'pasta'}
print(f"The alien color is {alien_0['color']}.")

alien_0['color'] = 'red'
print(f"My favorite food is {alien_0['food']}.")
#In this way to modify the values of dictonary.

alien_0 = {'color': 'red', 'food': 'pizza'}
print(alien_0)
alien_0['x_position'] = 0
alien_0['x_position'] = 25
print(alien_0)
#This method is used to add elements to a dictonary.


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Alien's original position{alien_0['x_position']}")
#Think about two point based number system.This system is actually working like the same.The alien is moving rightside.

if alien_0['speed'] == 'slow':
    x_increment = 1
#This statement defines that if the alien's speed is slow then the position will change 1 unit everytime.
elif alien_0['speed'] == 'modium':
    x_increment = 2
    #This statement defines that if the alien's speed is medium then the position will change 2 unit everytime.
else:
    x_increment = 3
#This statement defines that if the alien's speed is medium then the position will change 3 unit everytime.
#This line below indicates the position counting method of the alien.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"The new position of alien is{alien_0['x_position']}.")

#Removing a value
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(alien_0)

del alien_0['x_position']
print(alien_0)
#del function actually works for delating a value from a dictionary.

