favorite_language = {'Jeba': 'python', 'Soikot': 'Java script', 'monamee': 'CSS'}
language = favorite_language['Jeba'].title()
print(f"Jeba's favorite language is {language}"

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

favorites = {'food': 'pizza', 'ponts': 5}
mama = favorites.get('cloths', 'No point value assigned.')
print(mama)

fav_0 = {'Jeba': 'python', 'Soikot': 'java script', 'pial':'R', 'kaium': 'java'}
for name, language in fav_0.items():
    print(f"{name.title()}'s favorite programming language is {language.title()}")
