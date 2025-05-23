multiples = [value*3 for value in range(3, 30)]
print(multiples)



cubes = [value ** 3 for value in range(1, 11)]
print(cubes)


digits = []
for value in range(1, 21):
    cube = value ** 3
    digits.append(cube)
    print(digits)
# This code creates a list of cubes of numbers from 1 to 20




cubes = [value ** 3 for value in range(1, 21)]
print(cubes)