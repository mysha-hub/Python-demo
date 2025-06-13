
pizza = input("What is your favorite pizza topping?")
while True:
    if pizza == "pepperoni":
        print(f"We have {pizza} pizza!")
    elif pizza == "mushrooms":
        print(f"We have {pizza} pizza!")
    elif pizza == "pineapple":
        print(f"We have {pizza} pizza!")
    elif pizza == "anchovies":
        print(f"We have {pizza} pizza!")
    elif pizza == "cheese":
        print(f"We have {pizza} pizza!")
    elif pizza == "sausage":
        print(f"Sorry, we don't have {pizza} pizza.")
    
    else:
        break  # Exit the loop if the topping is not recognized
