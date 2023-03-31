#strings are immutable 
a = "! sangeetha ! ! sangeetha"
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!")) # removes (!) any trailing characters and does not skip leading ones
print(a.replace("sangeetha", "jadamal"))
print(a.split(" "))
greeting = "hello worLD"
print(greeting.capitalize())
print(a.count("sangeetha"))
print(a.endswith("!"))
print(a.isalnum())
print("********")
print(a.startswith("!"))#checks if the string starts with a given value. If yes then return True, else return False.

str1 = "welcome to python"
print(str1.endswith("python"))
print(str1.find("to")) # returns the index of first occurance and returns -1  if not there
print(str1.find("tooo"))

print(str1.title())#The title() method capitalizes each letter of the word within the string.

print(str1.endswith("to", 4, 10))
print(len(str1))
print(str1.center(25))
print(len(str1.center(25)))
print(str1.isalnum()) #returns ture if entire string consists of A-Z a-z 0-9

print(str1.isalpha()) # returns ture if the entire string consists of A-Z a-z

print(str1.islower())#returns if all the characters are lower

print(str1.isprintable())#returns True if all the values within the given string are printable, if not, then return (\n) False.
print(str1.isspace())#eturns True only and only if the string contains white spaces, else returns False.

str2 = "Hello World"
print(str2.istitle()) #returns True only if the first letter of each word of the string is capitalized, else it returns False.
print(str2.swapcase())#The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

str3 = "SANGEETHA"
print(str3.isupper)#returns True if all the characters in the string are upper case, else it returns False.

