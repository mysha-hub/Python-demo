fav_language = {'jeba': 'python', 'soikot': 'java script', 'david': 'c++', 'safia': 'R'}
for name in fav_language.keys():
    print(f"Hi, {name.title()} ")


list = ['jeba', 'mala', 'zen', 'soikot']
if name in list:
    language = fav_language[name].title()
    print(f"{name.title} loves {language}")
