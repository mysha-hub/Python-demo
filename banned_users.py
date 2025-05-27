banned_users = ['andrew', 'carolina', 'david']
user = input("Enter your name: ")
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print("sorry,you can not post a response.")