rows=int(input("number of rows: "))
ascii_value=int(input("enter the ascii value : "))
for i in range(rows):
    for j in range(i+1):
        alphabet=chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value = ascii_value + 1
    print()