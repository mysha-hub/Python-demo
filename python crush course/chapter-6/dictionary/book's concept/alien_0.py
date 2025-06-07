alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)




# Make an empty list for storing aliens.
alien = []

#make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alien.append(new_alien)
    

#show the first 5 aliens.
for alien in alien[:5]:
    print(alien)
print("...")


#Make an empty list for storing aliens.
aliens = []
#make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[0:5]:
    print(alien)
print("...")



print("\nHere is the starting of a new program.")
#make a empty alien list.
alien = []
#make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alien.append(new_alien)
#show the first 5 aliens.
for alien in alien[:5]:
    print(alien)
print("........")
print(f"Total number of aliens: {len(alien)}")
