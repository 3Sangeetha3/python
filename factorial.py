num = int(input("Enter the value num ="))
factorial = 1
if num <0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)


#using recursion method    
# Python recursion is a method which calls itself.

"""
def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  
  
num = 5  
print("Factorial of",num,"is",)  
fact(num))
"""

#using built_in function

"""
import math  
def fact(n):  
    return(math.factorial(n))  
  
num = int(input("Enter the number:"))  
f = fact(num) 
print("Factorial of", num, "is", f)  
"""
