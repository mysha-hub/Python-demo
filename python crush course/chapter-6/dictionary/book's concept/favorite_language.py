
favorite_language = {'Jeba': 'python', 'Soikot': 'Java script', 'monamee': 'CSS'}
language = favorite_language['Jeba'].title()
print(f"Jeba's favorite language is {language}")



fav_0 = {'Jeba': 'python', 'Soikot': 'java script', 'pial':'R', 'kaium': 'java'}
for name, language in fav_0.items():
    print(f"{name.title()}'s favorite programming language is {language.title()}")
for name in fav_0.keys():#this loop tells python to pull the keys from the dictonary.
    print(name.title())

friends = ['soikot', 'david', 'jay']
for name in fav_0.keys():
    print(f"Hello, {name.title()}")

if name in friends:
    language = fav_0[name].title()
    print(f"{name.title()},I see you love {language}")



#I can also use keys()mathod to know the person was polled or not.
if "Erin" not in fav_0.keys():
    print("Erin,please take our poll.")
