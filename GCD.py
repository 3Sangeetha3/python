#program to find the GCD of given inputs x and y
x = int(input('x: '))
y = int(input('y: '))

if x == 0 or y == 0:
    print('value must be non zero')
else:
    while y != 0:
        x, y = y, x % y
    print(f'gcd: {x}')

# alternative method with fruitful function
''' 
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

x = int(input('x: '))
y = int(input('y: '))

result = gcd(x, y)

print(result, 'using fruitful function')
'''