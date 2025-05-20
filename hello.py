name = input("What is your name?")#Ask user for their name.
print(name)
#say hello to user
print("Hello,", name)
name = name.capitalize()#capitalize the first letter of the name
name = name.strip()#remove white space
print(f"Hello, {name}")