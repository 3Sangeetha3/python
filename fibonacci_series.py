#Calculate Fibonacci series one number less than the given input x, and also calculate the sum of all alternate numbers (Even-numbered) in the resultant list. 
n = int(input("n: "))

#initialize variables
a = 0
b = 1

#iterate until a is less than or equal to n
while a <= n:
    #print a
    print(a)
    #calculate next number in fibonacci series
    c = a + b
    #update a and b
    a = b
    b = c