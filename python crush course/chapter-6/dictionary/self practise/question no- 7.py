alien_0 = {'user name': 'jeba', 'first name': 'mysha afrin', 'last name': 'jeba', 'location': 'dhaka'}
alien_1 = {'user name': 'soikot', 'first name': 'soikot', 'last name': 'rahman', 'location': 'chittagong'}
alien_2 = {'user name': 'david', 'first name': 'david', 'last name': 'smith', 'location': 'new york'}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(f"\nuser name: {alien['user name']}")
    full_name = f"{alien['first name']} {alien['last name']}"
    location = alien['location']
    print(f"Full name: {full_name.title()}")
    print(f'Location: {location.title()}')
