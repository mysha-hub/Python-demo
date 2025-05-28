alien_color = input("Enter the alien color (green, yellow, red): ")
if alien_color == 'green':
    print("Yahoo,you earned 5 points.")
else:
    print("oops!")
#exercise5-3
alien_color = "Yellow"
if alien_color == "Yellow":
    print("Yahoo,you earn 10 point.")
else:
    print("Oops")

#exercise5-5
alien_color = "Red"
if alien_color == "Red":
    print("You earned 10 points")
elif alien_color == "Yellow":
    print("You earned 15 ponts")
elif alien_color == "Green":
    print("You earned 5 points")
else:
    print("Ooops")


#exercise 5-6
age = int(input("Enter your age:"))
if age <= 2:
    print("The person is baby.")
elif age <= 4 and age > 2:
    print("The person is toddler.")
elif age <= 13 and age > 4:
    print("THe person is a kid.")
elif age <= 20 and age > 13:
    print("The person is a teenager.")
elif age <= 65 and age > 20:
    print("The person is a adult.")
else:
    print("The person is older.")
