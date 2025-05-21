score = int(input("Enter score:"))
if score >= 80 and score <= 100:
    print("Grade A")
elif score >=60 and score < 80:
    print("Grade B")
elif score >= 40 and score < 60:
    print("Grade C")
else:
    print("Failed")