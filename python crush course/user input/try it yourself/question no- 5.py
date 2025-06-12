prompt = "Enter your age : "
prompt += "I will show you your ticket price."
while True:
    age = int(input(prompt))
    if age < 3:
        print("Your ticket is free.")
    elif age < 12 and age >= 3:
        print("Your ticket is $10.")
    elif age >= 12:
        print("Your ticket is $15.")
