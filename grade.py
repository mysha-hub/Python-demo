score = int(input("Enter score:"))
if score >= 80 and score <= 100:
    print("Grade A")
elif score >=60 and score < 80:
    print("Grade B")
elif score >= 40 and score < 60:
    print("Grade C")
else:
    print("Failed")

a = 5 + 4j 
b = 10 + 9j 
c =  a + b
print(c)
print(type(c))


score = int(input("Enter score:"))
if 80 <= score <= 100:
    print("Grade A")
elif 60 <= score < 80:
    print("Grade B")
elif 40 <= score < 60:
    print("Grade C")
else:
    print("Failed")