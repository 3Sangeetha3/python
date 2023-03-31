def square(x):
    return x * x

def double(x):
    return x * 2

num = int(input('num: '))

result = square(double(num))

print('double, squaring the value:', result)


'''Function composition:

It combines functions in a way that the return value of each function is passed as an argument of the next function.

Let's consider an example:
Consider two functions f_1 and f_2.
Composition of two functions f_1 and f_2 is denoted f_1(f_2(x)).
* x is the argument of f_2.
The return value of f_2 is passed as an argument to f_1.
The result of the composition is the return value of f_1.
Follow the instructions and write the missing code in the below program.
* In the below program two functions square and double are defined with an argument x.
* Find the composition of two functions square(double(num)) and print the result.
* Take the input from the user.'''