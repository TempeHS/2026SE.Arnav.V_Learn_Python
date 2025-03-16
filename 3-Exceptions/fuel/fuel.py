x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

if x > y or y == 0:
    print('Retry!')
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
decimal = x / y
percentage = decimal * 100

if percentage >= 99:
    print('F')
elif percentage <= 1:
    print('E')
else:
    print(f"{percentage}%")