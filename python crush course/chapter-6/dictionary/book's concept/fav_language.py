favorite_languages = {'jen': 'python','sarah': 'c','edward': 'rust','phil': 'python',}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

#Idention should not be in code.If there is any identation error the code will not work.
