x = int(input("What's your score?"))
if x >= 80 and x <= 100:
    print("Grade A+")
elif x >= 70 and x < 80:
    print("Grade A")
elif x >= 60 and x < 70:
    print("Grade A-")
elif x >= 50 and x < 60:
    print("Grade B")
elif x >= 40 and x < 50:
    print("Grade C")
elif x >= 33 and x < 40:
    print("Grade D")
elif x >= 0 and x < 33:
    print("Grade F")
else:
    print("Soikot is a bungi")
# The code above is a simple grading system that takes an input score and assigns a grade based on the score range.