print("prefect number")
'''
n: 6
factors: [1, 2, 3]
perfect number
n: 32
factors: [1, 2, 4, 8, 16]
not perfect number
A number is called a perfect number if the sum of all its factors (excluding itself) is equal to the number
'''
# a program to print a prefect number 
n = int(input("n: "))
factors = []
for i in range(1, n//2+1):
    if n % i == 0:
        factors.append(i)
print("factors:", factors)
if sum(factors)==n:
    print("perfect number")
else: 
    print("not a perfect number")