'''
Take an integer n from the user using input() function. Write a program to print the the value of Pi up to n decimals. Print the result as shown in the example.

Sample Input and Output:
n: 5
3.1
3.14
3.142
3.1416
3.14159
'''
import math
pi = math.pi

n = int(input("n: "))
for i in range(1, n+1):
    print(f"{pi:.{i}f}")