x = int(input("What's x?"))
y = int(input("What's y?"))

if x > y:
    print(f'{y} is less than {x}')
elif x < y:
    print(f'{x} is less than {y}')
else:
    print(f'{x} is equal to {y}')