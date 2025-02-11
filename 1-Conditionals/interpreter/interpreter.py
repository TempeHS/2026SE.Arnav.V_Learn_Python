x, y, z = input('Math? ').split()
x = int(x)
z = int(z)

if y == '+':
    result = (x + z)
elif y == '-':
    result = (x - z)
elif y == 'x' or y == '*':
    result = (x * z)
elif y == '/':
    result = (x / z)
else:
    print(fore.RED +"ERROR")
print(f'{result:.1f}')