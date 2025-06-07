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



