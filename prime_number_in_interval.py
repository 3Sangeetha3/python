x = int(input("x: "))
y = int(input("y: "))

#iterate over range of numbers from x to y+1
for num in range(x,y+1):
    #check if num is greater than 1
    if num > 1:
        #initialize flag variable
        flag = True
        #iterate over range of numbers from 2 to num//2+1
        for i in range(2,num//2+1):
            #check if num is divisible by i
            if num % i == 0:
                #set flag to False
                flag = False
                #break out of loop
                break
        #check if flag is True
        if flag:
            #print num
            print(num)