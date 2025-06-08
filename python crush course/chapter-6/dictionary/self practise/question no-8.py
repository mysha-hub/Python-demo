pet_1 = {'username': 'jeba', 'pet name': 'dog,cat',}
pet_2 = {'username': 'soikot', 'pet name': 'cat,fish',}
pet_3 = {'username': 'monamee', 'pet name': 'dog,cat,fish',}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print(f"\nUsername: {pet['username'].title()}")
    print(f"\t\nPet name: {pet['pet name'].title()}")
