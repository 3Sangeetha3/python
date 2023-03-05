n = int(input("n: "))
digit  = n
for i in range(n,0,-1):
    for j in range(0, i):
        print(digit, end=" ")
    print("\n")
        