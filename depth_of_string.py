print("depth of string")

'''Program to check the depth and correctness of parenthesis

Write a program that checks for matching parenthesis, and prints an error if they do not match. Print the depth (nesting level) if they match as shown in the examples.

Sample Input and Output 1:
str: (())
valid and depth: 2

Sample Input and Output 2:
str: ()))
not valid and errors: 2'''

s = input("str: ")

#initialize variables
depth = 0
max_depth = 0
errors = 0

#iterate over characters in string
for c in s:
    #check if character is opening parenthesis
    if c == '(':
        #increment depth
        depth += 1
        #update max_depth
        max_depth = max(max_depth, depth)
    #check if character is closing parenthesis
    elif c == ')':
        #check if depth is greater than 0
        if depth > 0:
            #decrement depth
            depth -= 1
        else:
            #increment errors
            errors += 1

#check if depth is not 0
if depth != 0:
    #increment errors by depth
    errors += depth

#check if errors is greater than 0
if errors > 0:
    #print not valid and number of errors
    print("not valid and errors:", errors)
else:
    #print valid and max_depth
    print("valid and depth:", max_depth)