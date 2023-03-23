print("********** calculator **********")

num1 = input("Enter the value of num1 : ")
num2 = input("Enter the value of num2 : ")

print("""
Choose an operation from the list:
1. Addition
2. Subtraction
3. Multiplication
4. Exponentiation
5. Division
6. modulus
7. floor division
""")

option = int(input("Enter the number from above list : "))

if option == 1:
    print(f'{num1} + {num2} = {num1 + num2}')
elif option == 2:
    print(f'{num1} - {num2} = {num1 - num2}')  
elif option == 3:
    print(f'{num1} * {num2} = {num1 * num2}')
elif option == 4:
    print(f'{num1} ** {num2} = {num1 ** num2}')
elif option == 5:
    print(f'{num1} / {num2} = {num1 / num2}') 
elif option == 6:
    print(f'{num1} % {num2} = {num1 % num2}')
elif option == 7:
    print(f'{num1} // {num2} = {num1 // num2}')
else:
    print("Enter the valid number")