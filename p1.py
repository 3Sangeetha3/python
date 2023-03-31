#a program to print all the numbers less than a given number whether they are even or odd using a while loop
x = int(input('x: '))
i = 0
while i < x:
    if i % 2 == 0:
        print(f"{i} even number")
    else:
        print(f"{i} odd number")
    i+=1 