
fav_language = {'jeba': 'python', 'jen': 'python','sarah': 'c','edward': 'rust',}
friends = ['soikot', 'david', 'sarah']
for name in fav_language.keys():
    print(f"Dear {name.title()}, thanks for taking our poll")
    if name in friends:
        language = fav_language.keys()
        print(f"{name.title()} Please take our poll")
