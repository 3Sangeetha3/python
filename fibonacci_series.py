#Calculate Fibonacci series one number less than the given input x, and also calculate the sum of all alternate numbers (Even-numbered) in the resultant list. 
x = int(input('x: '))
a, b = 0, 1
total_sum = 0
i = 0
while a < x:
    print(a)
    if i % 2 == 0:
        total_sum += a
    a, b = b, a + b
    i += 1
print(f'sum: {total_sum}')