#code to find sum of all even numbers up to num using while construct
num = int(input("num: "))
sum = 0
i = 0
while i <= num:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
print(f'sum: {sum}')
