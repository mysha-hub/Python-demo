current_number = 1
while current_number <= 5:
    print("Current number is:", current_number)
    current_number += 1
current_number = 1
while current_number <= 100:
    print(f"{current_number}. I LOVE python!")
    current_number += 1
#This code will print the numbers from 1 to 5 and then print "I LOVE python!" 100 times, each time with the current number in front of it.
# The first loop counts from 1 to 5, printing the current number each time.


#counting odd numbers 1 to 100
counting_number = 1
while counting_number < 100:
    counting_number +=1
    if counting_number % 2 == 0:
        continue
    print(counting_number)
# This code will print all odd numbers from 1 to 100


x = 1
while x <= 10:
    print(x)
    x += 1
# This code will print numbers from 1 to 10, one number per line.


# a forever loop
x = 1
while x <= 10:
    print(x)
    # x += 1  # Uncommenting this line will stop the loop
