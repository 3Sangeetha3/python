#a program to find the sum of all integers between 0 and num, both inclusive.
num = int(input("num : "))
total_sum = 0
i = 0
if num >= 0:
    while i <= num:
        total_sum += i
        i += 1
else:
    while i >= num:
        total_sum += i
        i -= 1
print(f'sum: {total_sum}')