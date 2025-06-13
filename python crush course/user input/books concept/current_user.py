#start with users that need to be verified
#an empty list to hold the users
unconfirmed_users = ['alice', 'brian', 'candace']
#an empty list to hold the confirmed users
confirmed_users = []
#verify each user until there are no more unconfirmed users
while unconfirmed_users:
    #pop the first user from the list
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    #add the user to the confirmed users list
    confirmed_users.append(current_user)
#display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
