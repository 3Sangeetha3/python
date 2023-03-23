print("'0' for exit")

#take ch input from the user
ch = input('ch: ')
if (ch == '0'):
    exit()
elif ch.isnumeric():
    print('digit')
elif ch.isalpha():
    print('alphabet')
else:
    print('neither alphabet nor digit')