users = {'alice' : {'first name':'alice', 'last name':'smith', 'location':'new york'}, 
            'jeba' : {'first name':'mysha afrin', 'last name':'jeba', 'location':'dhaka'}, 
            'soikot' : {'first name':'soikot', 'last name':'rahman', 'location':'chittagong'}}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first name']} {user_info['last name']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
